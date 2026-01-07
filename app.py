import streamlit as st
import google.genai as genai

while True:
   user_input = input("You: ")
   if user_input.lower() == "exit":
       print("Bot: Goodbye!")
      break
try:
    # Streamlit automatically loads secrets as env vars
    client = genai.Client()

    st.write("Gemini API client configured.")

    prompt = "Benefits of API key management?"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    st.write(response.text)

except Exception as e:
    st.error(f"Error: {e}")
