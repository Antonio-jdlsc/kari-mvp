import openai


def generate_prompt(message):
    # Hacer una llamada a la API de ChatGPT para generar preguntas complementarias
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Estás : {message}",
        max_tokens=50,
        n=3,
        stop=None,
        temperature=0.7
    )

    # Obtener las preguntas generadas de la respuesta de la API
    prompts = [choice['text'] for choice in response.choices]

    return prompts
