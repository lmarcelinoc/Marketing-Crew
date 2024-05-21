import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Write a blog post about the benefits of AI in marketing."
    print(generate_text(prompt))
