from flask import Flask
from flask_restful import Api
from resources import gvision_route, twilio_route, upload_image_route
import config

app = Flask(__name__)
api = Api(app)


api.add_resource(upload_image_route.ImageUpload, '/upload')
api.add_resource(gvision_route.GVisionRoute, '/vision')
api.add_resource(twilio_route.Twilio, '/twilio')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def server_error(e):
    print("error")
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=True
    )
