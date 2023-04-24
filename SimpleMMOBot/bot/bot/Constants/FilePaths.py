import os
from enum import Enum

class FilePaths(Enum):
    CREDENTIALS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/InitializingBot/credentials.txt')
    CHROME_ARGUMENTS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/InitializingBot/arguments.txt')
    
    BOT_STATUS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/Discord/status.txt')

    LOGS = os.path.join(os.getcwd(), 'SimpleMMOBot/bot/bot/Files/Logger/logs.txt')