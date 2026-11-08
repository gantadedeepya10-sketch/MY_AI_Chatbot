def chatbot(message):

    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome!"

    elif "how are you" in message:
        return "I am doing great!"

    elif "name" in message:
        return "My name is Python Bot."

    elif "college" in message:
        return "I can help you with your studies!"

    elif "thanks" in message:
        return "You are welcome!"

    else:
        return "Sorry, I don't know that yet."