from Managers.Files.FileManager import FileManager
from Constants.WebsitePaths import WebsitePaths
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Constants.Expressions import Expressions

class LoginManager:
    def input_email(element_handler, email):
        email_input_locator = By.NAME
        email_input_expression = Expressions.EMAIL_INPUT.value
        element_handler.wait_for_element_and_send_input(
            expected_condition=EC.visibility_of_element_located,
            locator_type=email_input_locator,
            expression_type=email_input_expression,
            text=email
        )

    def input_password(element_handler, password):
        password_input_locator = By.NAME
        password_input_expression = Expressions.PASSWORD_INPUT.value
        element_handler.wait_for_element_and_send_input(
            expected_condition=EC.visibility_of_element_located,
            locator_type=password_input_locator,
            expression_type=password_input_expression,
            text=password
        )

    def click_login_button(element_handler):
        login_button_locator = By.CSS_SELECTOR
        login_button_expression = Expressions.LOGIN_BUTTON.value
        element_handler.find_and_click_on_element(
            locator_type=login_button_locator,
            expression_type=login_button_expression
        )


    def wait_until_travel_page_is_loaded(element_handler, chrome_handler):
        take_a_step_locator = By.XPATH
        take_a_step_expression = Expressions.TAKE_STEP_BUTTON.value
        take_a_step_condition = EC.visibility_of_any_elements_located
        chrome_handler.go_to_page(WebsitePaths.TRAVEL_PAGE.value, element_handler, take_a_step_condition, take_a_step_locator, take_a_step_expression)

    def login(chrome_handler, element_handler, email, password):
        FileManager.update_bot_current_action(status_text="Trying to login")
        LoginManager.input_email(element_handler, email)
        LoginManager.input_password(element_handler, password)
        LoginManager.click_login_button(element_handler)
        LoginManager.wait_until_travel_page_is_loaded(element_handler, chrome_handler)
        FileManager.update_bot_current_action(status_text="Logged in successfully")