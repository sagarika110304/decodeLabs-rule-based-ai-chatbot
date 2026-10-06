"""
Project 1: Rule-Based AI Chatbot
DecodeLabs - Artificial Intelligence Training

A simple rule-based chatbot using if-else logic and a continuous loop.
"""

def chatbot():
    print("=" * 50)
    print("       Rule-Based AI Chatbot 🤖")
    print("=" * 50)
    print("Hello! I'm a simple AI chatbot.")
    print("You can say hello, ask my name, or ask how I am.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["hello", "hi", "hey", "hii"]:
            print("Bot: Hello! Nice to meet you! 😊")

        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking. How are you?")

        elif "your name" in user_input or user_input == "name":
            print("Bot: I'm a Rule-Based AI Chatbot.")

        elif "who are you" in user_input:
            print("Bot: I'm a simple chatbot created using Python if-else logic.")

        elif "help" in user_input:
            print("Bot: You can greet me, ask my name, ask how I am, or say bye.")

        elif user_input in ["bye", "exit", "quit", "goodbye"]:
            print("Bot: Goodbye! Have a great day! 👋")
            break

        elif user_input == "":
            print("Bot: Please type something so I can respond.")

        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()
