import streamlit as st
import google.genai as genai

st.title("Gemini Prompt Playground")

try:
    client = genai.Client()

    # User input
    user_prompt = st.text_area(
        "Enter your prompt:",
        placeholder="Ask Gemini anything..."
    )

    # Button to trigger API call
    if st.button("Generate Response"):
        if user_prompt.strip() == "":
            st.warning("Please enter a prompt.")
        else:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_prompt
            )
            st.subheader("Response")
            st.write(response.text)

except Exception as e:
    st.error(f"Error: {e}")
