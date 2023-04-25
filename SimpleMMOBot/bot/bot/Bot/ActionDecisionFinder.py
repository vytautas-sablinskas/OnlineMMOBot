from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions

class ActionDecisionFinder:
    def __init__(self, element_handler):
        self.element_handler = element_handler
        self.element = None
        self.next_action = "None"

    def find_next_action(self, logged_in):
        if not logged_in:
            self.next_action = "Login"
            return

        afk_verification_element = self.element_handler.find_element(By.LINK_TEXT, Expressions.CONFIRM_EXISTENCE_BUTTON.value)
        if afk_verification_element and afk_verification_element.is_enabled():
            self.element = afk_verification_element
            self.next_action = "AFK Verification"
            return
        
        attack_mob_element = self.element_handler.find_element(By.LINK_TEXT, Expressions.ATTACK_MOB_PAGE_LINK.value)
        if attack_mob_element and attack_mob_element.is_enabled():
            self.element = attack_mob_element
            self.next_action = "Attack Mob"
            return
        
        take_step_element = self.element_handler.find_element(By.XPATH, Expressions.TAKE_STEP_BUTTON.value)
        if take_step_element and take_step_element.is_enabled():
            self.element = take_step_element
            self.next_action = "Step"
            return
        
        self.element, self.next_action = None, "None"
        