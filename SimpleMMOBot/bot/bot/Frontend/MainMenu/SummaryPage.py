import sys 
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '...', 'Backend'))
sys.path.append(backend_dir)

import streamlit as st
import numpy as np
from Handlers.FileHandler import FileHandler
from Handlers.TextHandler import TextHandler
from Constants.FilePaths import FilePaths

def show_action_counts():
    action_lines = FileHandler.read_from_file_lines(FilePaths.SESSION_ACTION_SUMMARY.value)
    action_df = TextHandler.split_actions_summary(action_lines)
    action_df.index = np.arange(1, 9)
    st.header("Actions done in this session")
    st.table(action_df)

def show_page(script_status):
    if script_status != "Running":
        st.header("Script is not running! No information to show.")
        return
    
    show_action_counts()
