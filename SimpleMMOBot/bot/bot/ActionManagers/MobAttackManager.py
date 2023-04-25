from selenium.webdriver.common.by import By
from Constants.Expressions import Expressions
from Constants.WebsitePaths import WebsitePaths
from ActionManagers.VerificationManager import VerificationManager
from ActionManagers.FileManager import FileManager

class MobAttackManager:
    @staticmethod
    def attack_mob_until_dead(link_to_mob_attack_page, element_handler, discord_model):
        element_handler.go_to_page_by_clicking_element(link_to_mob_attack_page)
        mob_is_alive = True
        while mob_is_alive:
            FileManager.update_status("Attacking mob")
            MobAttackManager.click_attack_mob(element_handler)

            VerificationManager.check_for_afk_verification(discord_model)

            battle_has_ended = MobAttackManager.check_for_battle_end_element()
            if battle_has_ended:
                element_handler.go_to_page(WebsitePaths.TRAVEL_PAGE.value)
                mob_is_alive = False

    def click_attack_mob(element_handler):
        mob_was_attacked = element_handler.find_and_click_on_element(
            locator_type=By.XPATH,
            expression_type=Expressions.ATTACK_MOB_BUTTON.value
        )

        return mob_was_attacked

    def check_for_battle_end_element(element_handler):
        battle_has_ended = element_handler.find_element(
            locator_type=By.LINK_TEXT,
            expression_type=Expressions.BATTLE_HAS_ENDED.value
        )
        return battle_has_ended