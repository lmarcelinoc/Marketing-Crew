import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

if __name__ == "__main__":
    prompt = "A futuristic city with flying cars"
    print(generate_image(prompt))
