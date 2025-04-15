from listen import get_audio
from respond import get_response
from speak import say

def main():
    print("🧠 Smart AI Assistant Ready! Say 'exit' to stop.")
    while True:
        user_input = get_audio()
        print(f"🗣️ You said: {user_input}")

        if user_input.lower() in ["exit", "quit", "stop"]:
            say("Goodbye!")
            break

        reply = get_response(user_input)
        print(f"🤖 Assistant: {reply}")
        say(reply)

if __name__ == "__main__":
    main()
