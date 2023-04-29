import sys 
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '...', 'Backend'))
sys.path.append(backend_dir)

import streamlit as st
import numpy as np
from Managers.Files.FileManager import FileManager
from Handlers.TextHandler import TextHandler

def show_action_counts():
    action_lines = FileManager.get_session_summary()
    action_df = TextHandler.split_actions_summary(action_lines)
    action_df.index = np.arange(1, 9)
    st.header("Actions done in this session")
    st.table(action_df)

def show_page(script_status):
    if script_status != "Running":
        st.header("Script is not running! No information to show.")
        return
    
    show_action_counts()
