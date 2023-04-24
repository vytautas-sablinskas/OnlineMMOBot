import Handlers.ChromeDriverHandler as ChromeDriverHandler

class Initializer:
    def __init__(self):
        self.driver = ChromeDriverHandler.ChromeDriverHandler().driver