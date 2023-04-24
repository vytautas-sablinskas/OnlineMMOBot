from . import Initializer

class ActionController:
    def __init__(self):
        self.initializer = Initializer.Initializer()

    def login(self):
        print(self.initializer.user.email)
        