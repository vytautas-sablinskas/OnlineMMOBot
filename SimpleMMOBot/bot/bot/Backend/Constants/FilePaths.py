import os
from enum import Enum

class FilePaths(Enum):
    IMPORT_REQUIREMENTS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/InitializingBot/import_requirements.txt')
    DISCORD_BOT = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/DiscordBot.py')
    CREDENTIALS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/InitializingBot/credentials.txt')
    CHROME_ARGUMENTS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/InitializingBot/arguments.txt') 
    DISCORD_CREDENTIALS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/Discord/discord_credentials.txt')
    BOT_STATUS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/Discord/bot_status.txt')
    CURRENT_BOT_ACTION = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/Discord/current_action.txt')
    FILE_HANDLER = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Handlers/FileHandler.py')
    ACTION_TRACKING_LOGS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/Information/action_tracking_logs.txt')
    BOT_START = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/main.py')
    PANEL_BOT_STATUS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/Information/panel_status.txt')
    SESSION_ACTION_SUMMARY = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Backend/Files/Information/session_action_summary.txt')