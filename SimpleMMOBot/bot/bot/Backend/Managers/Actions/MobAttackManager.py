from .VerificationManager import VerificationManager
from Managers.Files.FileManager import FileManager
from Managers.Navigation.PageNavigator import PageNavigator
from Managers.Navigation.ButtonClicker import ButtonClicker
from Managers.Navigation.ButtonLocator import ButtonLocator


class MobAttackManager:
    def check_mob_is_alive(chrome_handler, element_handler):
        battle_has_ended = ButtonLocator.check_battle_ended_link_exists(element_handler)
        if battle_has_ended:
            PageNavigator.go_to_travel_page(chrome_handler, element_handler)
            return False
        
        return True

    def fight_mob_until_defeated(mob_attack_page, chrome_handler, element_handler, discord_model):
        ButtonClicker.click_button_to_new_page_and_update_status(
            mob_attack_page, 
            "Attacking Mob"
        )

        mob_is_alive = True
        while mob_is_alive:
            FileManager.update_bot_current_action("Attacking mob")
            ButtonClicker.click_attack_mob(element_handler)

            verification_link_found = VerificationManager.check_for_afk_verification(
                chrome_handler,
                element_handler, 
                discord_model
            )
            if verification_link_found:
                return

            mob_is_alive = MobAttackManager.check_mob_is_alive(chrome_handler, element_handler)
