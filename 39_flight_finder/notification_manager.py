from twilio.rest import Client
import os

TWILIO_SID = 'ACc9604759e58a2cc4a1570d9fdd82724c' 
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH")
TWILIO_VIRTUAL_NUMBER = "+17652075906"
TWILIO_VERIFIED_NUMBER = "+18329935448"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)