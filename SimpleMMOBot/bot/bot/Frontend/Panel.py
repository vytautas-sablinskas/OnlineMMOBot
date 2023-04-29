import sys
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend'))
sys.path.append(backend_dir)

import streamlit as st
from streamlit_option_menu import option_menu
import MainMenu.StartupPage as StartupPage

def set_sidebar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Script Launcher", "Script Information"]
        )
        
    if selected == "Script Launcher":
        StartupPage.show_page()
    elif selected == "Script Information":
        running_script()



def running_script():
    st.write("Hello, it's the running script tab.")

def main():
    st.set_page_config(page_title="SimpleMMO Bot", page_icon=":robot_face:", layout="wide")
    set_sidebar()

if __name__ == "__main__":
    main()