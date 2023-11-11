
import streamlit as st
import openai
from dotenv import load_dotenv
load_dotenv()
import os
openai.api_key = os.getenv("OPENAI_KEY")

def get_response(text):
    prompt = f"""
           You are an expert in writing of stories. You'll be given a text delimited by four backwquotes, 
           Make sure to meet the main points, and giving more detailes about the charecters. it should be fully story any one can understand.
           Your story should be informative and well structured, the story consisting of 10 to 15 sentences.

           text: ````{text}````
           """
    
    
    response = openai.Completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens=2000
    )
    return response['choices'][0]['text']

def app():
    st.title("Story Writing :speech_balloon:")
    input=st.text_area("Describe the story you want to write:")
    if st.button('Send'):
        if input:
            with st.spinner('Wait for it...'): 
                response = get_response(input)
            st.markdown(response)
        else:
            st.write("You didn't upload any file.")

