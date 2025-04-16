import os
from dotenv import load_dotenv
from voice_agent.respond import get_response
from voice_agent.speak import say

load_dotenv()

print("Smart Assistant — type to chat, type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        say("Goodbye!")
        break

    reply = get_response(user_input)
    print(f"Assistant: {reply}\n")
    say(reply)
