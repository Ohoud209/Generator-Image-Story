import streamlit as st
def app():
    add_selectbox = st.selectbox(
        " :thought_balloon: Which contact method is your preference?",
        ("Email", "LinkedIn")
    )
    if add_selectbox == "Email":
        st.write(" :love_letter: ohoud27@gmail.com")
    if add_selectbox == "LinkedIn":
        if st.button("Click on the following link to view my profile:scroll:", type="primary"):
            st.write("https://www.linkedin.com/in/ohoud-saleh-86352324b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app")
        

