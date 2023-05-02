from Handlers.ChromeDriverHandler import ChromeDriverHandler
from Handlers.ElementHandler import ElementHandler
from Managers.Files.FileManager import FileManager
from Managers.Timers.BreakManager import BreakManager
from Managers.Actions.ItemManager import ItemManager
from Bot.DecisionMaker import DecisionMaker
from Models.User import User
from Models.Discord import Discord
from Constants.FilePaths import FilePaths

class Initializer:
    def initialize_item_manager():
        return ItemManager()

    def initialize_break_manager():
        playtime = FileManager.get_playtime_before_sleep()
        return BreakManager(playtime)

    def initialize_chrome_driver():
        return ChromeDriverHandler()
    
    def initialize_element_handler(driver):
        return ElementHandler(driver)

    def initialize_decision_maker(element_handler):
        return DecisionMaker(element_handler)

    def initialize_user_class(user_credentials_path=FilePaths.CREDENTIALS.value):
        email, password = FileManager.get_user_or_discord_credentials(user_credentials_path)
        user = User(email, password)
        return user
    
    def initialize_discord_class(discord_credentials_path=FilePaths.DISCORD_CREDENTIALS.value):
        webhook_url, token = FileManager.get_user_or_discord_credentials(discord_credentials_path)
        discord = Discord(token, webhook_url)
        return discord