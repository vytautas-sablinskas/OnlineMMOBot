import sys 
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '...', 'Backend'))
sys.path.append(backend_dir)

import pandas as pd
import numpy as np
import streamlit as st
from Managers.Files.FileManager import FileManager

def get_last_ten_actions():
    action_logs = FileManager.get_action_tracking_logs()
    last_ten_actions = action_logs[-10:]
    df = pd.DataFrame(last_ten_actions, columns=['Actions and their execution time'])
    return df

def show_current_action():
    current_action = FileManager.get_current_bot_action()
    st.header("Current action:")
    st.write(current_action)

def show_last_ten_actions():
    last_ten_actions = get_last_ten_actions()[::-1]
    last_ten_actions.index = np.arange(1, 11)
    st.subheader("Last 10 Actions")
    st.table(last_ten_actions)

def show_page(script_status):
    if script_status.lower() != "running":
        st.header("Script is not running! No information to show.")
        return

    st.subheader("Information about running script.")
    show_current_action()
    show_last_ten_actions()
