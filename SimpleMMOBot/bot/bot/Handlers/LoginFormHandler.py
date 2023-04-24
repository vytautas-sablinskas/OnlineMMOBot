from Constants.Expressions import Expressions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginFormHandler:
    def __init__(self, element_handler, user):
        self.element_handler = element_handler
        self.user = user

    def input_email(self):
        email_input_locator = By.NAME
        email_input_expression = Expressions.EMAIL_INPUT.value
        self.element_handler.wait_for_element_and_send_input(
            expected_condition=EC.visibility_of_element_located,
            locator_type=email_input_locator,
            expression_type=email_input_expression,
            text=self.user.email
        )

    def input_password(self):
        password_input_locator = By.NAME
        password_input_expression = Expressions.PASSWORD_INPUT.value
        self.element_handler.wait_for_element_and_send_input(
            expected_condition=EC.visibility_of_element_located,
            locator_type=password_input_locator,
            expression_type=password_input_expression,
            text=self.user.password
        )

    def click_login_button(self):
        login_button_locator = By.CSS_SELECTOR
        login_button_expression = Expressions.LOGIN_BUTTON.value
        self.element_handler.find_and_click_on_element(
            locator_type=login_button_locator,
            expression_type=login_button_expression
        )