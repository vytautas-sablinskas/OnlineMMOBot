from . import ActionController

class Bot:
    def __init__(self):
        self.action_controller = ActionController.ActionController()

    def run(self):
        self.action_controller.login()
        self.action_controller.take_action()