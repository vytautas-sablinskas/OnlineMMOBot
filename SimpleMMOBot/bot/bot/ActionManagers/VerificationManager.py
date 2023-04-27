from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions
from Constants.WebsitePaths import WebsitePaths
from Constants.Messages import Messages
from Constants.FilePaths import FilePaths
from Handlers.FileHandler import FileHandler
from Handlers.TextHandler import TextHandler
from ActionManagers.FileManager import FileManager
import time


class VerificationManager:
    def pause_script_until_manually_continued():
        waiting_for_user_to_unpause = True
        while waiting_for_user_to_unpause:
            user_response = FileHandler.read_from_file_lines(
                FilePaths.BOT_STATUS.value
            )
            bot_status = TextHandler.get_bot_status(user_response)
            if bot_status == "Continue":
                waiting_for_user_to_unpause = False

    @staticmethod
    def inform_about_afk_verification(discord_model):
        discord_model.send_message_to_discord_server(Messages.AFK_VERIFICATION.value)
        VerificationManager.pause_script_until_manually_continued()

    @staticmethod
    def check_for_afk_verification(chrome_handler, element_handler, discord_model, action):
        verification_link_popped_up = element_handler.find_element(
            locator_type=By.LINK_TEXT,
            expression_type=Expressions.PRESS_VERIFY_BUTTON.value
        )

        if verification_link_popped_up:
            FileManager.update_bot_status(status_text="Paused")
            VerificationManager.inform_about_afk_verification(discord_model)
            if action != "Step":
                chrome_handler.driver.get(WebsitePaths.TRAVEL_PAGE.value)
                time.sleep(1)