import streamlit as st
from streamlit_option_menu import option_menu

def set_sidebar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Script Launcher", "Script Information"]
        )
        
    if selected == "Script Launcher":
        bot_startup()
    elif selected == "Script Information":
        running_script()

def bot_startup():
    st.header('Welcome to SimpleMMO Bot')
    st.write("Hello, it's the bot startup tab.")

def running_script():
    st.write("Hello, it's the running script tab.")

def main():
    st.set_page_config(page_title="SimpleMMO Bot", page_icon=":robot_face:", layout="wide")
    set_sidebar()

if __name__ == "__main__":
    main()