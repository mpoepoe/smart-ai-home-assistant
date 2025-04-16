import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Session memory stores the conversation
conversation_history = [
    {"role": "system", "content": (
        "You are my smart home assistant. You can remember what we talk about in this session. "
        "Answer questions, help with daily tasks, and respond like a friendly voice assistant."
    )}
]

def get_response(prompt):
    # Add user input to memory
    conversation_history.append({"role": "user", "content": prompt})

    # Call GPT
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=conversation_history,
        max_tokens=300
    )

    # Get GPT's reply and store it
    reply = response.choices[0].message.content.strip()
    conversation_history.append({"role": "assistant", "content": reply})
    return reply
