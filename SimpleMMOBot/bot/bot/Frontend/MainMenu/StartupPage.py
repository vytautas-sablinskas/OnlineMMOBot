import sys 
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '...', 'Backend'))
sys.path.append(backend_dir)

import streamlit as st
import psutil
import numpy as np
import subprocess
from Managers.Files.FileManager import FileManager
from Constants.FilePaths import FilePaths

process = None

def get_user_credential_input_fields():
    email, password =  FileManager.get_user_or_discord_credentials(FilePaths.CREDENTIALS.value)
    email_input_box = st.text_input("Email", value=email, placeholder="Enter SimpleMMO Account Email")
    password_input_box = st.text_input("Password", value=password, type='password', placeholder="Enter SimpleMMO Account Password")
    return email_input_box, password_input_box

def get_discord_credential_input_fields():
    discord_webhook_url, discord_token = FileManager.get_user_or_discord_credentials(FilePaths.DISCORD_CREDENTIALS.value)
    discord_webhook_url_box = st.text_input("Discord Webhook URL", value=discord_webhook_url, placeholder="Enter Discord Webhook URL")
    discord_token_box = st.text_input("Discord Bot Token", value=discord_token, placeholder="Enter Discord Bot Token")
    return discord_webhook_url_box, discord_token_box

def get_argument_values(headless_mode, mute_audio):
    arguments_to_add = []

    if headless_mode:
        arguments_to_add.append("--headless=new")

    if mute_audio:
        arguments_to_add.append("--mute-audio")

    return arguments_to_add

def get_argument_checkboxes():   
    st.markdown("""
                <style>
                [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
                    gap: 0rem;
                }
                </style>
                """,
                unsafe_allow_html=True
    )
    st.header("Select Browser Options")    
    headless_mode = st.checkbox("Headless mode(No browser GUI) | Works in background")
    mute_audio = st.checkbox("Mute Audio | Tab will have no audio")
    return headless_mode, mute_audio

def get_playtime_until_break():
    playtime_options = np.arange(0, 301)
    playtime = st.select_slider("Select after how many minutes to take break. If selected 0 - No breaks", options=playtime_options)
    print(f"first playtime: {playtime}")
    return playtime

def run_bot(email, password, discord_webhook_url, discord_token, chrome_arguments, playtime):
    FileManager.update_user_credentials(email, password)
    FileManager.update_discord_credentials(discord_webhook_url, discord_token)
    FileManager.update_chrome_arguments(chrome_arguments)
    FileManager.update_playtime_until_break(playtime)
    
    process = subprocess.Popen(["python", FilePaths.BOT_START.value])
    st.success("Bot successfully started")
    return process

def stop_bot(process):  
    parent = psutil.Process(process.pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    parent.kill()
    print("Bot successfully stopped!")
    st.success("Bot successfully stopped!")

def show_page(script_status):
    global process

    st.header('Welcome to SimpleMMO Bot')
    st.write('Enter information and settings')
    
    email_input_box, password_input_box = get_user_credential_input_fields()
    discord_webhook_url_box, discord_token_box = get_discord_credential_input_fields()
    headless_mode, mute_audio = get_argument_checkboxes()
    playtime = get_playtime_until_break()

    start_button_place, stop_button_place = st.columns(spec=2, gap="small")
    run_button = start_button_place.button(label="Start bot")
    stop_button = stop_button_place.button(label="Stop bot")

    if run_button:
        if script_status.lower() != "stopped":
            st.info("Bot is already running!")
            return
        
        input_fields_not_filled = len(email_input_box) <= 0 or len(password_input_box) <= 0 or len(discord_webhook_url_box) <= 0 or len(discord_token_box) <= 0
        if input_fields_not_filled:
            st.error("Fill in all input fields | Checkboxes are not necessary")
            return

        chrome_arguments = get_argument_values(headless_mode, mute_audio)
        process = run_bot(email_input_box, password_input_box, discord_webhook_url_box, discord_token_box, chrome_arguments, playtime)
        script_status="Running"
        FileManager.update_panel_bot_status(script_status)
    
    if stop_button:
        if script_status.lower() != "running" or process is None:
            st.info("Bot is already not running!")
            return
        
        stop_bot(process)
        script_status="Stopped"
        FileManager.update_panel_bot_status(script_status)