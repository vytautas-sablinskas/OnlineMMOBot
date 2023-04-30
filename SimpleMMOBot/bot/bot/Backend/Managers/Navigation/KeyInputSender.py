from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Constants.Expressions import Expressions
from Managers.Navigation.ButtonLocator import ButtonLocator
from Handlers.ElementHandler import ElementHandler


class KeyInputSender:
    def input_email_keys(element_handler, email):
        email_input_field = ButtonLocator.check_email_input_field_exists(element_handler)
        element_handler.send_input_to_element(email_input_field, email)

    def input_password_keys(element_handler, password):
        password_input_field = ButtonLocator.check_password_input_field_exists(element_handler)
        element_handler.send_input_to_element(password_input_field, password)