print("=== Simple Chatbot ===")
print("Type 'bye' to exit the chat.\n")
while True:
    user_input = input("You: ").lower()
    if user_input == "hello":
        print("Bot: Hi")
    elif user_input == "how are you":
        print("Bot: I'm Fine, Thanks!")
    elif user_input == "bye":
        print("Bot: Goodbye!...")
        break
    else:
        print("Bot: Sorry, I don't understand that.")