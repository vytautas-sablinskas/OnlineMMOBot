from . import Initializer
from Constants.FilePaths import FilePaths
from Constants.WebsitePaths import WebsitePaths
from Constants.Expressions import Expressions
from Handlers.TimeHandler import TimeHandler
from Handlers.FileHandler import FileHandler
from Handlers.ElementHandler import ElementHandler
from Handlers.LoginFormHandler import LoginFormHandler
from .ActionDecisionMaker import ActionDecisionMaker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.common.exceptions as ex
import time

class ActionController:
    def __init__(self):
        self.initializer = Initializer.Initializer()
        self.element_handler = ElementHandler(self.initializer.driver)
        self.login_form_handler = LoginFormHandler(self.element_handler, self.initializer.user)
        self.action_decision_maker = ActionDecisionMaker(self.element_handler)

    def update_status(self, status_text, file_path=FilePaths.BOT_STATUS):
        current_datetime = TimeHandler.get_current_datetime()
        status = f"Bot status: {status_text}, Last Updated: {current_datetime}"
        FileHandler.write_into_file(file_path, status)

    def login(self):
        self.update_status(status_text="Trying to login")
        self.login_form_handler.input_email()
        self.login_form_handler.input_password()
        self.login_form_handler.click_login_button()
        self.initializer.driver.get(WebsitePaths.TRAVEL_PAGE.value)
        self.login_form_handler.wait_until_travel_page_is_loaded()
        self.update_status(status_text="Logged in successfully")

    def take_steps(self, take_step_button):
        TimeHandler.sleep_for_random_time(0.1, 1.6)
        if take_step_button.is_enabled():
            self.update_status(status_text="Taking steps")
            take_step_button.click()


    def take_action(self):
        user_wants_bot_to_run = True
        while user_wants_bot_to_run:
            self.action_decision_maker.find_next_action()
            next_action = self.action_decision_maker.next_action
            element = self.action_decision_maker.element
            if next_action == "Step":
                self.take_steps(take_step_button=element)
            if next_action == "None":
                time.sleep(1)
