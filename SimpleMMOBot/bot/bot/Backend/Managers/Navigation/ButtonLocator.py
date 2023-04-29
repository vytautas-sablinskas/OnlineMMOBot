from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions

class ButtonLocator:
    def check_battle_ended_link_exists(element_handler):
        battle_has_ended_locator = By.LINK_TEXT
        battle_has_ended_expression = Expressions.BATTLE_HAS_ENDED.value
        battle_has_ended_link_exists = element_handler.find_element(
            locator_type=battle_has_ended_locator,
            expression_type=battle_has_ended_expression
        )

        return battle_has_ended_link_exists
    
    def check_press_verify_button_exists(element_handler):
        verify_button_locator = By.LINK_TEXT
        verify_button_expression = Expressions.PRESS_VERIFY_BUTTON.value    
        press_verify_button_exists = element_handler.find_element(
            locator_type=verify_button_locator,
            expression_type=verify_button_expression
        )

        return press_verify_button_exists
    
    def check_press_gather_button_exists(element_handler):
        gather_button_locator = By.ID
        gather_button_expression = Expressions.GATHER_BUTTON.value
        gather_button_exists = element_handler.find_element(
                locator_type=gather_button_locator, 
                expression_type=gather_button_expression
        )

        return gather_button_exists