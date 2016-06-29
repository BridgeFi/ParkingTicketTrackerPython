from flask_restful import Resource
from flask import request
from google_vision import text_index
from common import json_responses as json


class GVisionRoute(Resource):

    def post(self):
        req = request.form.get('file_path')
        # Start text_index script for text detection
        text_index.main(req)
        # Get Index class for getting response variable
        index = text_index.Index()
        response = index.response

        if response:
            if response["status"].startswith("error"):
                # handle error
                return response
            data = parse_text(response)
            if data:
                return json.success_response(data, "Text detected successfully")
            else:
                return json.error_response("No relevant data found", "400")


# Parsing detected text
def parse_text(response):
    for item in response["data"]:
        return item.decode("UTF-8").splitlines()
