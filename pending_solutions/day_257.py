import requests

def get_response(user_input):
    url = "https://example.com/chatbot"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "message": user_input
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("response", "I'm sorry, I didn't understand that.")

def chatbot():
    print("Welcome to the Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        bot_response = get_response(user_input)
        print(f"Chatbot: {bot_response}")

if __name__ == "__main__":
    chatbot()