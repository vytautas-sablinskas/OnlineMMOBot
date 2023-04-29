from Handlers.ChromeDriverHandler import ChromeDriverHandler
from Handlers.FileHandler import FileHandler
from Handlers.TextHandler import TextHandler
from Handlers.ElementHandler import ElementHandler
from Managers.Files.FileManager import FileManager
from Bot.ActionDecisionMaker import ActionDecisionMaker
from Models.User import User
from Models.Discord import Discord
from Constants.FilePaths import FilePaths

class Initializer:
    def initialize_chrome_driver():
        return ChromeDriverHandler()
    
    def initialize_element_handler(driver):
        return ElementHandler(driver)

    def initialize_action_decision_maker(element_handler):
        return ActionDecisionMaker(element_handler)

    def initialize_user_class(user_credentials_path=FilePaths.CREDENTIALS.value):
        email, password = FileManager.get_user_or_discord_credentials(user_credentials_path)
        user = User(email, password)
        return user
    
    def initialize_discord_class(discord_credentials_path=FilePaths.DISCORD_CREDENTIALS.value):
        webhook_url, token = FileManager.get_user_or_discord_credentials(discord_credentials_path)
        discord = Discord(token, webhook_url)
        return discord