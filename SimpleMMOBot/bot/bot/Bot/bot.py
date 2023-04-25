from ActionManagers.LoginManager import LoginManager
from Bot.ActionController import ActionController

class Bot:
    def __init__(self):
        self.action_controller = ActionController()

    def run(self):
        self.action_controller.take_action_depending_on_current_screen()