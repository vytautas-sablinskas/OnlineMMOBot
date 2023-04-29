from Constants.Messages import Messages
from Managers.Files.FileManager import FileManager
from Managers.Navigation.ButtonLocator import ButtonLocator
from Managers.Navigation.PageNavigator import PageNavigator
from Managers.Files.FileManager import FileManager

class VerificationManager:
    def wait_for_user_to_resume_script():
        script_is_paused = True
        while script_is_paused:
            bot_status = FileManager.get_bot_status()
            if bot_status.lower() == "continue":
                script_is_paused = False

    def notify_user_about_afk_verification(chrome_handler, element_handler, discord_model):
        FileManager.update_bot_status(status_text="Paused")
        discord_model.send_message_to_discord_server(Messages.AFK_VERIFICATION.value)
        VerificationManager.wait_for_user_to_resume_script()
        PageNavigator.go_to_travel_page(chrome_handler, element_handler)

    def check_for_afk_verification(chrome_handler, element_handler, discord_model):
        afk_verification_link_found = ButtonLocator.check_press_verify_button_exists(element_handler)
        if not afk_verification_link_found:
            return afk_verification_link_found

        FileManager.update_bot_status(status_text="Paused")
        VerificationManager.notify_user_about_afk_verification (chrome_handler, element_handler, discord_model)
        
        return afk_verification_link_found
                