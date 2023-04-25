from Constants.Expressions import Expressions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ActionManagers.FileManager import FileManager
from ActionManagers.VerificationManager import VerificationManager
from Constants.WebsitePaths import WebsitePaths

class MaterialGatheringManager:
    def get_gathering_actions():
        gathering_actions = ["Grab", "Salvage", "Catch", "Chop", "Mine"]
        return gathering_actions

    def click_gather_button_until_close(chrome_handler, element_handler, discord_model):
        materials_can_be_gathered = True
        attempts = 0
        while materials_can_be_gathered:
            attempts += 1
            VerificationManager.check_for_afk_verification(
                element_handler, discord_model)
            gather_button = element_handler.find_element(
                By.ID, Expressions.GATHER_BUTTON.value)
            
            if gather_button and "close" in gather_button.text.lower():
                print("closing")
                chrome_handler.go_to_page(WebsitePaths.TRAVEL_PAGE.value, element_handler, expected_condition=EC.visibility_of_any_elements_located,
                                          locator_type=By.XPATH, expression_type=Expressions.TAKE_STEP_BUTTON.value)
                materials_can_be_gathered = False
            elif gather_button and gather_button.is_enabled():
                gather_button.click()
            elif attempts > 10:
                break

    def gather_materials(chrome_handler, element_handler, action, link_to_material_gathering_page, discord_model):
        gathering_level_too_low = element_handler.find_element(
            By.XPATH, Expressions.GATHERING_LEVEL_TOO_LOW.value)
        if gathering_level_too_low:
            return "Step"

        FileManager.update_status(
            status_text=f"Gathering materials, Action: {action}")
        element_handler.go_to_page_by_clicking_element(
            link_to_material_gathering_page)
        MaterialGatheringManager.click_gather_button_until_close(
            chrome_handler, element_handler, discord_model)
