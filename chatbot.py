# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()# normalize input into lower alphabets for easier comparison

    #Conditionals
    if "hello" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye! Talk to you later."
    else:
        return "Sorry, I don't understand that."
# Chat function
def chat():
    print("Chatbot: Hello! Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
        if "bye" in user_input.lower():
            break

# Start chatting
chat()
