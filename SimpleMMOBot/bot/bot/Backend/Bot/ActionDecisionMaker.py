from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions
from Managers.Actions.MaterialGatheringManager import MaterialGatheringManager

class ActionDecisionMaker:
    def __init__(self, element_handler):
        self.element_handler = element_handler
        self.element = None
        self.next_action = "None"
        self.gathering_action = "None"

    def find_next_action(self, logged_in, action_counter):
        if not logged_in:
            self.next_action = "Login"
            return

        afk_verification_element = self.element_handler.find_element(By.LINK_TEXT, Expressions.CONFIRM_EXISTENCE_BUTTON.value)
        if afk_verification_element and afk_verification_element.is_enabled():
            self.element = afk_verification_element
            self.next_action = "AFK Verification"
            action_counter["AFK Checks"] += 1
            return
        
        attack_mob_element = self.element_handler.find_element(By.LINK_TEXT, Expressions.ATTACK_MOB_PAGE_LINK.value)
        if attack_mob_element and attack_mob_element.is_enabled():
            self.element = attack_mob_element
            self.next_action = "Attack Mob"
            action_counter["Mobs Attacked"]
            return

        gathering_level_too_low = self.element_handler.find_element(By.XPATH, Expressions.GATHERING_LEVEL_TOO_LOW.value)  
        if not gathering_level_too_low:
            gathering_actions = MaterialGatheringManager.get_gathering_actions()
            for action in gathering_actions:
                action_element = self.element_handler.find_element(By.XPATH, Expressions.LINK_TO_GATHERING_PAGE.value.format(action))
                if action_element and action_element.is_enabled():
                    self.element = action_element
                    self.next_action = "Gather Materials"
                    self.gathering_action = action    
                    action_counter[action] += 1
                    return       
        
        take_step_element = self.element_handler.find_element(By.XPATH, Expressions.TAKE_STEP_BUTTON.value)
        if take_step_element and take_step_element.is_enabled():
            self.element = take_step_element
            self.next_action = "Step"
            action_counter["Steps Taken"] += 1
            return
        
        self.element, self.next_action, self.gathering_action = None, "None", "None"
        