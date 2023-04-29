from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Constants.Expressions import Expressions

class KeyInputSender:
    def input_email_keys(element_handler, email):
        email_input_locator = By.NAME
        email_input_expression = Expressions.EMAIL_INPUT.value
        element_handler.wait_for_element_and_send_input(
            expected_condition=EC.visibility_of_element_located,
            locator_type=email_input_locator,
            expression_type=email_input_expression,
            text=email
        )

    def input_password_keys(element_handler, password):
        password_input_locator = By.NAME
        password_input_expression = Expressions.PASSWORD_INPUT.value
        element_handler.wait_for_element_and_send_input(
            expected_condition=EC.visibility_of_element_located,
            locator_type=password_input_locator,
            expression_type=password_input_expression,
            text=password
        )