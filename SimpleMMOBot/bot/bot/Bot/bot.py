import importlib
import subprocess
from Bot.ActionController import ActionController
from Constants.FilePaths import FilePaths

class Bot:
    def __init__(self):
        self.action_controller = ActionController()

    def check_dependencies():
        packages = ['package1', 'package2', 'package3']
        for package_name in packages:
            try:
                importlib.import_module(package_name)
            except ImportError:
                print(f"Error: {package_name} is not installed. Installing now...")
                install_package(package_name)

    def run_discord_bot_in_parallel(self):
        discord_token = self.action_controller.discord.token
        subprocess.Popen(['python', FilePaths.DISCORD_BOT.value, discord_token])

    def run_mmo_bot(self):
        self.run_discord_bot_in_parallel()
        self.action_controller.take_action_depending_on_current_screen()