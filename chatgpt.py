import config
import openai


class ChatGPT:
    def __init__(self):
        self.api_key = config.CHATGPT_API_KEY

    def generate_response(self, message, prompt):
        openai.api_key = self.api_key

        # Concatenar el mensaje y el prompt
        input_text = f"{message}\n{prompt}"

        # Generar la respuesta utilizando la API de ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        if response.choices:
            return response.choices[0].text.strip()
        else:
            return None
