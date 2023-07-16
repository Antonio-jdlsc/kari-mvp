import config
from twilio.rest import Client


class WhatsAppBot:
    def __init__(self):
        self.client = Client(config.TWILIO_SID, config.TWILIO_AUTH_TOKEN)
        self.whatsapp_number = config.WHATSAPP_NUMBER

    def send_message(self, recipient, message):
        self.client.messages.create(
            from_=f"whatsapp:{self.whatsapp_number}",
            body=message,
            to=f"whatsapp:{recipient}"
        )

