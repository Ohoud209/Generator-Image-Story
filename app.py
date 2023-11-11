import streamlit as st
import openai
# from streamlit_option_menu import option_menu
import generat
import map
import contact
st.set_page_config(
        page_title="Caption Generator",
)


def main():
    with st.sidebar:
        # selected = option_menu(
        #     menu_title="Options Menu",
        #     options=["Image Generator", "Image Captioning", "Contact"],
        #     icons = ["chat-right-text", "body-text", "envelope-at"],
        #     menu_icon="list",
        #     default_index=0,
        #     orientation="virtical",
        #     styles={
        #         "container": {"padding": "0!important", "background-color": "#ebd2b9"},
        #         "icon": {"color": "white", "font-size": "15px"},
        #         "nav-link": {
        #             "font-size": "25px",
        #             "text-align": "left",
        #             "margin": "0px",
        #             "--hover-color": "#919e8b",
        #         },
        #         "nav-link-selected": {"background-color": "#919e8b"},
        #     },
        # )
        selected = ['Image Generator', 'Story Writing', 'Contact']
        selected_option = st.selectbox(' :fog: Options Menu', selected)
    if selected_option == 'Image Generator':
            generat.app()
    if selected_option == 'Story Writing':
           map.app()    
    if selected_option == 'Contact':
            contact.app()    


if __name__:
    main()
