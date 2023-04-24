from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions

class ActionDecisionMaker:
    def __init__(self, element_handler):
        self.element_handler = element_handler
        self.element = None
        self.next_action = "None"

    def find_next_action(self):
        take_step_element = self.element_handler.find_element(By.XPATH, Expressions.TAKE_STEP_BUTTON.value)
        if take_step_element and take_step_element.is_enabled():
            self.element = take_step_element
            self.next_action = "Step"
        
        return None, "None"
