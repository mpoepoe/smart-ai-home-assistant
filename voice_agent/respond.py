import openai

openai.api_key = "your-api-key-here"

def get_response(prompt):
    messages = [
        {"role": "system", "content": "You're a friendly kitchen assistant. Give helpful food and recipe tips."},
        {"role": "user", "content": prompt}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=300
    )
    return completion.choices[0].message.content.strip()
