from openai import OpenAI

def get_image(prompt, key):
    openai_client = OpenAI(api_key=key)
    response = openai_client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size='1024x1024',
                    quality="standard",
                    n=1
    )

    return response.data[0].url   