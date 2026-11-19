
def chatbot():
    print("\nHelloUtil AI Chatbot")
    print("Type 'exit' to leave")

    while True:
        message = input("\nYou: ")

        if message.lower() == "exit":
            break

        if "hello" in message.lower():
            print("AI: Hello! Welcome to HelloUtil")

        elif "help" in message.lower():
            print("AI: What do you need help with?")

        else:
            print("AI: I'm still learning! More AI functionality coming soon")
