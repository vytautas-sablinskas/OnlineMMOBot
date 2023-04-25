from Handlers.ChromeDriverHandler import ChromeDriverHandler
from Handlers.FileHandler import FileHandler
from Handlers.TextHandler import TextHandler
from Handlers.ElementHandler import ElementHandler
from Bot.ActionDecisionFinder import ActionDecisionFinder
from Models.User import User
from Models.Discord import Discord
from Constants.FilePaths import FilePaths

class Initializer:
    def initialize_chrome_driver():
        return ChromeDriverHandler()
    
    def initialize_element_handler(driver):
        return ElementHandler(driver)

    def initialize_action_decision_finder(element_handler):
        return ActionDecisionFinder(element_handler)

    def initialize_user_class(user_credentials_path=FilePaths.CREDENTIALS.value):
        credential_lines = FileHandler.read_from_file_lines(user_credentials_path)
        email, password = TextHandler.split_credentials(credential_lines)
        user = User(email, password)
        return user
    
    def initialize_discord_class(discord_credentials_path=FilePaths.DISCORD_CREDENTIALS.value):
        credential_lines = FileHandler.read_from_file_lines(discord_credentials_path)
        webhook_url, token = TextHandler.split_credentials(credential_lines)
        discord = Discord(token, webhook_url)
        return discord