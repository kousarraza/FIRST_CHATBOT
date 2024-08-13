import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Configure the API key from Streamlit secrets
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interfacepi
st.set_page_config(page_title="Simple ChatBot🤖", layout="centered")

st.markdown("""
    <style>
        .container { background-color: blue; color: white; padding: 20px; }
    </style>
    <div class="container">
        <h1 style='text-align: center;'>👾 Simple ChatBot 🤖</h1>
        <h2 style='text-align: center;'>by Kousar Raza 👽</h2>
    </div>
    """, unsafe_allow_html=True)


st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
        color: black;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5; color: black;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background-color: #e1ffc7; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
        color: black;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5; color: black;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)
    
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please Enter A Prompt")