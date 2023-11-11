import streamlit as st
import openai
from streamlit.elements.spinner import spinner
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
import os
openai.api_key = st.secrets["OPENAI_KEY"]
def get_response(user_prompt):
    
    
    response = openai.Image.create(
        prompt = user_prompt,
        n = 1,
        size =  "1024x1024"
    )
    return response.data[0].url



def app():
    st.title("Image Generator :bridge_at_night:")
    text = st.text_input("Write a description of an image:", "here")
    r = st.button("Send")
    if r and text!=None:
        with spinner("Generating your image..."):
            t = get_response(text)
        st.image(t, width=200)

