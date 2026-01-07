from google import genai

# 🔑 Put your Gemini API key directly here
API_KEY = "AIzaSyCRwFiyRo1wpCQBBS0YHKKZQsdFIvMpIGk"

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Start a chat session
chat = client.chats.create(model="gemini-2.5-flash")

print("Gemini Chat (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    response = chat.send_message(user_input)
    print("Gemini:", response.text)
