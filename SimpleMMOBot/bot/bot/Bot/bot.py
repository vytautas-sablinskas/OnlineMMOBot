import ActionController

class Bot:
    def __init__(self):
        self.bot = ActionController()    
    def start(self):
        self.bot.login()
        self.bot.perform_actions()