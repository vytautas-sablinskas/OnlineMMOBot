import sys 
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '...', 'Backend'))
sys.path.append(backend_dir)

import streamlit as st
import psutil
import subprocess
from Handlers.FileHandler import FileHandler
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

def run_bot(email, password, discord_webhook_url, discord_token, chrome_arguments):
    FileHandler.write_into_file(file_path=FilePaths.CREDENTIALS.value,
                                data=f"{email}\n{password}"
    )

    FileHandler.write_into_file(file_path=FilePaths.DISCORD_CREDENTIALS.value,
                                data=f"{discord_webhook_url}\n{discord_token}"
    )

    FileHandler.write_into_file(file_path=FilePaths.CHROME_ARGUMENTS.value,
                                data=chrome_arguments)
    
    process = subprocess.Popen(["python", FilePaths.BOT_START.value])
    st.success("Bot successfully started")
    return process

def stop_bot(process):
    if process is None:
        st.error("Bot hasn't started yet!")
        return
    
    parent = psutil.Process(process.pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    parent.kill()
    print("Bot successfully stopped!")
    st.success("Bot successfully stopped!")

def show_page():
    global process

    st.header('Welcome to SimpleMMO Bot')
    st.write('Enter information and settings')
    
    email_input_box, password_input_box = get_user_credential_input_fields()
    discord_webhook_url_box, discord_token_box = get_discord_credential_input_fields()

    headless_mode, mute_audio = get_argument_checkboxes()

    start_button_place, stop_button_place = st.columns(spec=2, gap="small")
    run_button = start_button_place.button(label="Start bot")
    stop_button = stop_button_place.button(label="Stop bot")

    if run_button:
        chrome_arguments = get_argument_values(headless_mode, mute_audio)
        process = run_bot(email_input_box, password_input_box, discord_webhook_url_box, discord_token_box, chrome_arguments)
    
    if stop_button:
        stop_bot(process)