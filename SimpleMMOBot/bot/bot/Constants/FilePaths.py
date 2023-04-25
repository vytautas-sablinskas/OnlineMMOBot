import os
from enum import Enum

class FilePaths(Enum):
    DISCORD_BOT = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/DiscordBot.py')
    CREDENTIALS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/InitializingBot/credentials.txt')
    CHROME_ARGUMENTS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/InitializingBot/arguments.txt') 
    DISCORD_CREDENTIALS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/Discord/discord_credentials.txt')
    BOT_STATUS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/Discord/bot_status.txt')
    CURRENT_BOT_ACTION = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/Discord/current_action.txt')
    LOGS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/Logger/logs.txt')
    FILE_HANDLER = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Handlers/FileHandler.py')