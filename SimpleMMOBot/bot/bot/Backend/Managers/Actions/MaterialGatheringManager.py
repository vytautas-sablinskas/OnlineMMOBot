from Constants.Expressions import Expressions
from selenium.webdriver.common.by import By
from Managers.Files.FileManager import FileManager
from Managers.Actions.VerificationManager import VerificationManager
from Handlers.TimeHandler import TimeHandler

class MaterialGatheringManager:
    def get_gathering_actions():
        gathering_actions = ["Grab", "Salvage", "Catch", "Chop", "Mine"]
        return gathering_actions

    def click_gather_button_until_close(chrome_handler, element_handler, discord_model):
        materials_can_be_gathered = True
        while materials_can_be_gathered:
            verification_popped = VerificationManager.check_for_afk_verification(
                chrome_handler,
                element_handler, 
                discord_model
            )
            if verification_popped:
                return

            gather_button = element_handler.find_element(
                By.ID, Expressions.GATHER_BUTTON.value
            )
            if not gather_button:
                continue
     
            if "close" in gather_button.text.lower():
                gather_button.click()
                TimeHandler.sleep_for_random_time(1.5, 2)
                materials_can_be_gathered = False
            else:
                gather_button.click()
                TimeHandler.sleep_for_random_time(1, 1.2)

    def gather_materials(chrome_handler, element_handler, action, link_to_material_gathering_page, discord_model):
        FileManager.update_bot_current_action(status_text=f"Gathering materials, Action: {action}")
        element_handler.go_to_page_by_clicking_element(link_to_material_gathering_page)
        MaterialGatheringManager.click_gather_button_until_close(chrome_handler, 
                                                                 element_handler, 
                                                                 discord_model
        )