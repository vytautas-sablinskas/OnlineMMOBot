import Handlers.ChromeDriverHandler as ChromeDriverHandler
from Handlers.FileHandler import FileHandler
from Handlers.TextHandler import TextHandler
from Models import User
from Constants.FilePaths import FilePaths

class Initializer:
    def __init__(self):
        self.driver = ChromeDriverHandler.ChromeDriverHandler().driver
        email, password = self.get_credentials()
        self.user = User.User(email, password)

    def get_credentials(self, file_path=FilePaths.CREDENTIALS):
        credential_lines = FileHandler.read_from_file_lines(file_path)
        email, password = TextHandler.split_credentials(credential_lines)
        return email, password