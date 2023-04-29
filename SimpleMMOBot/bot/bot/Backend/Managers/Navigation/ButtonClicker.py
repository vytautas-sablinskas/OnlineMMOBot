from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions
from Managers.Files.FileManager import FileManager
from Handlers.ElementHandler import ElementHandler

class ButtonClicker:
    def click_login_button(element_handler):
        login_button_locator = By.CSS_SELECTOR
        login_button_expression = Expressions.LOGIN_BUTTON.value
        element_handler.find_and_click_on_element(
            locator_type=login_button_locator,
            expression_type=login_button_expression
        )

    def click_attack_mob(element_handler):
        attack_mob_locator = By.XPATH
        attack_mob_expression = Expressions.ATTACK_MOB_BUTTON.value

        mob_was_attacked = element_handler.find_and_click_on_element(
            locator_type=attack_mob_locator,
            expression_type=attack_mob_expression
        )

        return mob_was_attacked
    
    def click_button_to_new_page_and_update_status(action_button, new_status):
        ElementHandler.click_element(action_button)
        FileManager.update_bot_current_action(status_text=new_status)