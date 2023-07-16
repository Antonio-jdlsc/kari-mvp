import prompts
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, BOT_PHONE_NUMBER
from twilio.rest import Client
from chatgpt import ChatGPT


class WhatsAppBot:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.bot_number = BOT_PHONE_NUMBER
        self.chatgpt = ChatGPT()

    def send_message(self, recipient, message):
        message = self.client.messages.create(
            from_=self.bot_number,
            body=message,
            to=recipient
        )
        return message

    def process_message(self, sender, message):
        # Obtener los prompts complementarios usando la función generate_prompt
        prompt = prompts.generate_prompt(message)

        # Generar la respuesta utilizando los prompts y la lógica existente
        response = self.generate_response(message, prompt)

        if response:
            self.send_message(sender, response)

    def generate_response(self, message, prompt):
        response = self.chatgpt.generate_response(message, prompt)  # Genera la respuesta utilizando la API de ChatGPT

        if response:
            return response
        else:
            return 'Lo siento, no puedo entender tu solicitud. Por favor, sé más específico.'


