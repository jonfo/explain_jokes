import streamlit as st
import openai
import os
from openai import OpenAI

# Set your OpenAI API key here or set environment variable OPENAI_API_KEY
#openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


st.title("Joke explainer")

joke = st.text_area("Enter a joke:")

if st.button("Submit"):
    if not joke.strip():
        st.warning("Please enter a joke.")
    else:
        with st.spinner("Explaining the joke..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        #{"role": "system", "content": "You are a helpful assistant that explains jokes in a clear and simple way."},
                        {"role": "user", "content": f"Explain this joke: {joke}"}
                    ],
                    max_tokens=150,
                    temperature=0.7,
                )
                explanation = response.choices[0].message.content
                st.subheader("Joke Explanation:")
                st.write(explanation)
            except Exception as e:
                st.error(f"Error communicating with OpenAI: {e}")