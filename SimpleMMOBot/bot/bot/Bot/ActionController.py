from . import Initializer
from Constants.FilePaths import FilePaths
from Constants.Expressions import Expressions
from Handlers.TimeHandler import TimeHandler
from Handlers.FileHandler import FileHandler
from Handlers.ElementHandler import ElementHandler
from Handlers.LoginFormHandler import LoginFormHandler
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.common.exceptions as ex

class ActionController:
    def __init__(self):
        self.initializer = Initializer.Initializer()
        self.element_handler = ElementHandler(self.initializer.driver)
        self.login_form_handler = LoginFormHandler(self.element_handler, self.initializer.user)

    def update_status(self, status_text, file_path=FilePaths.BOT_STATUS):
        current_datetime = TimeHandler.get_current_datetime()
        status = f"Bot status: {status_text}, Last Updated: {current_datetime}"
        FileHandler.write_into_file(file_path, status)

    def login(self):
        self.update_status(status_text="Trying to login")
        self.login_form_handler.input_email()
        self.login_form_handler.input_password()
        self.login_form_handler.click_login_button()