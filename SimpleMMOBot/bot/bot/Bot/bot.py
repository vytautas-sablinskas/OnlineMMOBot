import subprocess
import os
from Bot.ActionController import ActionController
from Constants.FilePaths import FilePaths

class Bot:
    def __init__(self):
        self.action_controller = ActionController()

    def run_discord_bot_in_parallel(self):
        discord_token = self.action_controller.discord.token
        subprocess.Popen(['python', FilePaths.DISCORD_BOT.value, discord_token])

    def run_mmo_bot(self):
        self.run_discord_bot_in_parallel()
        self.action_controller.take_action_depending_on_current_screen()