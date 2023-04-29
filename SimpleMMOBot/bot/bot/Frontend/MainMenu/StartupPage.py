import sys 
import os
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '...', 'Backend'))
sys.path.append(backend_dir)

import streamlit as st
from Handlers.FileHandler import FileHandler
from Managers.Files.FileManager import FileManager
from Constants.FilePaths import FilePaths

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

def run_bot(email, password, discord_webhook_url, discord_token):
    FileHandler.write_into_file(file_path=FilePaths.CREDENTIALS.value,
                                data=f"{email}\n{password}"
    )

    FileHandler.write_into_file(file_path=FilePaths.DISCORD_CREDENTIALS.value,
                                data=f"{discord_webhook_url}\n{discord_token}"
    )
    st.success("Bot successfully started")

def show_page():
    st.header('Welcome to SimpleMMO Bot')
    st.write('Enter information and settings')
    
    email_input_box, password_input_box = get_user_credential_input_fields()
    discord_webhook_url_box, discord_token_box = get_discord_credential_input_fields()

    run_button = st.button(label="Start bot")

    if run_button:
        run_bot(email_input_box, password_input_box, discord_webhook_url_box, discord_token_box)
    