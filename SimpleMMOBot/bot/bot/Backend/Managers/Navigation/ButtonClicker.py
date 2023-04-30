from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions
from Managers.Files.FileManager import FileManager
from Handlers.ElementHandler import ElementHandler
from Managers.Navigation.ButtonLocator import ButtonLocator

class ButtonClicker:
    def click_login_button(element_handler):
        login_button = ButtonLocator.check_login_button_exists(element_handler)
        ElementHandler.click_element(login_button)

    def click_attack_mob(element_handler):
        attack_mob_button = ButtonLocator.check_click_attack_mob_button_exists(element_handler)
        mob_was_attacked = ElementHandler.click_element(attack_mob_button)

        return mob_was_attacked
    
    def click_button_to_new_page_and_update_status(action_button, new_status):
        ElementHandler.click_element(action_button)
        FileManager.update_bot_current_action(status_text=new_status)