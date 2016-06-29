from flask_restful import Resource
from flask import request
from storage import upload_image
from common import json_responses as json


def upload_image_file(file_input):
    if not file_input:
        print("no file attached")
        return None

    public_url = upload_image.upload_file(
        file_input.read(),
        file_input.filename,
        file_input.content_type
    )
    print("public urL: "+public_url)

    return public_url


class ImageUpload(Resource):

    def post(self):
        print("upload beginning")
        data = request.form.to_dict(flat=True)
        img_url = upload_image_file(request.files.get('ticket_photo'))

        if img_url:
            data['imgUrl'] = img_url
            return json.success_response(img_url, "Image uploaded successfully")
        else:
            return json.error_response("Something went wrong while uploading image. Please try again later", "500")

