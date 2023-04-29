from Managers.Files.FileManager import FileManager
from Managers.Navigation.ButtonClicker import ButtonClicker
from Managers.Navigation.KeyInputSender import KeyInputSender
from Managers.Navigation.PageNavigator import PageNavigator

class LoginManager:
    def login(chrome_handler, element_handler, email, password):
        FileManager.update_bot_current_action(status_text="Trying to login")
        KeyInputSender.input_email_keys(element_handler, email)
        KeyInputSender.input_password_keys(element_handler, password)
        ButtonClicker.click_login_button(element_handler)
        PageNavigator.go_to_travel_page(chrome_handler, element_handler)
        FileManager.update_bot_current_action(status_text="Logged in successfully")