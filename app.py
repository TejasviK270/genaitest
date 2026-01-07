import streamlit as st
import google.genai as genai

try:
    # Streamlit automatically loads secrets as env vars
    client = genai.Client()

    st.write("Gemini API client configured.")

    prompt = input("")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.write(response.text)

except Exception as e:
    st.error(f"Error: {e}")
