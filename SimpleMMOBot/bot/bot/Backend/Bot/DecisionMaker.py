from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions
from Managers.Actions.MaterialGatheringManager import MaterialGatheringManager
from Managers.Navigation.ButtonLocator import ButtonLocator

class DecisionMaker:
    def __init__(self, element_handler):
        self.element_handler = element_handler
        self.element = None
        self.next_action = "None"
        self.gathering_action = "None"

    def check_for_afk_verification_action(self, action_counter):
        confirm_existence_button = ButtonLocator.check_confirm_existence_button_exists(self.element_handler)
        if confirm_existence_button and confirm_existence_button.is_enabled():
            self.element = confirm_existence_button
            self.next_action = "AFK Verification"
            action_counter["AFK Checks"] += 1
            return True

        return False

    def check_for_mob_attack_action(self, action_counter):
        attack_mob_link = ButtonLocator.check_attack_mob_link_exists(self.element_handler)
        if attack_mob_link and attack_mob_link.is_enabled():
            self.element = attack_mob_link
            self.next_action = "Attack Mob"
            action_counter["Mobs Attacked"] += 1
            return True
        
        return False
    
    def check_for_gathering_materials_action(self, action_counter):
        gathering_level_too_low = ButtonLocator.check_gathering_level_too_low(self.element_handler)
        if gathering_level_too_low:
            return False

        gathering_actions = MaterialGatheringManager.get_gathering_actions()
        for gathering_action in gathering_actions:
            gathering_action_link = ButtonLocator.check_gathering_link_exists(self.element_handler, gathering_action)
            if gathering_action_link and gathering_action_link.is_enabled():
                self.element = gathering_action_link
                self.next_action = "Gather Materials"
                self.gathering_action = gathering_action    
                action_counter[gathering_action] += 1
                return True

        return False   

    def check_for_taking_a_step_action(self, action_counter):
        take_step_button = ButtonLocator.check_take_a_step_button_exists(self.element_handler)
        if take_step_button and take_step_button.is_enabled():
            self.element = take_step_button
            self.next_action = "Step"
            action_counter["Steps Taken"] += 1
            return True
        
        return False

    def find_next_action(self, logged_in, action_counter):
        needs_to_login = not logged_in
        if needs_to_login:
            self.next_action = "Login"
            return

        afk_verification_is_next_action = self.check_for_afk_verification_action(action_counter)
        if afk_verification_is_next_action:
            return

        mob_attack_is_next_action = self.check_for_mob_attack_action(action_counter)
        if mob_attack_is_next_action:
            return

        gathering_materials_is_next_action = self.check_for_gathering_materials_action(action_counter)
        if gathering_materials_is_next_action:
            return
        
        take_a_step_is_next_action = self.check_for_taking_a_step_action(action_counter)
        if take_a_step_is_next_action:
            return
        
        self.element, self.next_action, self.gathering_action = None, "None", "None"
        