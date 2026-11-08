from ai_chatbot import ask_ai

print("Welcome to My AI Chatbot!")

while True:
    message = input("You: ")

    if message.lower().strip() == "bye":
        print("Bot: Goodbye!")
        break

    try:
        answer = ask_ai(message)
        print("Bot:", answer)

    except Exception as e:
        print("Something went wrong. Please check the AI connection.")