import streamlit as st
import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.environ["Gemini_API"])

# Function to get the AI model response
def get_response(user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    return response.text

# Set up session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 0;
        padding: 0;
    }
    .navbar {
        background-color: rgba(0, 132, 255, 0.8);
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        width: 100%;
        top: 0;
        z-index: 1000;
    }
    .navbar h1 {
        margin: 0;
        font-size: 24px;
        font-weight: bold;
    }
    .chat-container {
        width: 100%;
        max-width: 700px;
        margin-top: 70px;
    }
    .user-message {
        background-color: #0084ff;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: right;
        width: fit-content;
        max-width: 70%;
        margin-left: auto;
    }
    .bot-message {
        background-color: #e5e5ea;
        color: black;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: left;
        width: fit-content;
        max-width: 70%;
        margin-right: auto;
    }
    .input-area {
        width: 100%;
        margin-top: 20px;
    }
    .footer {
       background-color: rgba(0, 132, 255, 0.8);
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        width: 100%;
        top: 0;
        z-index: 1000;
    }
    .footer p {
        margin: 0;
        font-size: 14px;
        font-weight: bold;
    }
    .footer small {
        display: block;
        margin-top: 5px;
        font-size: 12px;
        color: white;
        border-radius:10px
    }
    </style>
""", unsafe_allow_html=True)

# Transparent Navbar
st.markdown("""
    <div class="navbar">
        <h1>Venus Ai</h1>
    </div>
""", unsafe_allow_html=True)

# Chat Interface
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Chat area
for message in st.session_state.messages:
    st.markdown(f"<div class='user-message'>{message['user_input']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-message'>{message['response']}</div>", unsafe_allow_html=True)

# Input area
user_input = st.text_input("Type your queries here...", key="input")
if st.button("Send"):
    if user_input:
        # Get response from the model
        response = get_response(user_input)
        
        # Add message to chat history
        st.session_state.messages.append({"user_input": user_input, "response": response})
        
        # Rerun the app to update the chat
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# Enhanced Footer
st.markdown("""
    <div class="footer">
        <p>Created by Shamroze Khan</p>
        <small>Powered by Gemini 1.5 Flash</small>
    </div>
""", unsafe_allow_html=True)
