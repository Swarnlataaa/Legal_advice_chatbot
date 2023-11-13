import streamlit as st
import openai

# Set your OpenAI GPT-3 API key
openai.api_key = "YOUR_API_KEY"

def legal_chatbot(prompt):
    # Generate a response from the chatbot
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can try other engines too
        prompt=prompt,
        temperature=0.7,  # Controls the randomness of the response
        max_tokens=150,   # Limit the length of the response
        n=1,              # Number of responses to generate
    )

    # Extract and return the generated response
    reply = response['choices'][0]['text'].strip()
    return reply

# Streamlit app
st.title("Legal Consultancy Chatbot")

# User input
user_input = st.text_area("Ask a legal question:")

# Button to trigger the chatbot response
if st.button("Get Legal Advice"):
    # Check if the user has entered a question
    if user_input:
        # Get a response from the chatbot
        bot_response = legal_chatbot(user_input)

        # Display the bot's response
        st.markdown(f"**Legal Chatbot:** {bot_response}")
    else:
        st.warning("Please enter a legal question.")
