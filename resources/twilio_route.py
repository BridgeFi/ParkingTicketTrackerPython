from flask_restful import Resource
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from common import json_responses as json
import config


class Twilio(Resource):

    account_sid = config.TEST_TWILIO_ACCOUNT_SID
    auth_token = config.TEST_TWILIO_AUTH_TOKEN
    twilio_number = config.TEST_TWILIO_NUMBER

    __client = TwilioRestClient(account_sid, auth_token)

    def get(self):
        print("get")

        try:
            print("Twilio start")
            self.__client.messages.create(
                body="Twilio msg",
                to="+14156919591",
                from_=self.twilio_number
            )
            return json.success_response("", "Message sent")
        except TwilioRestException as ex:
            return json.error_response("Message not sent, %s" % ex.msg, ex.status)
