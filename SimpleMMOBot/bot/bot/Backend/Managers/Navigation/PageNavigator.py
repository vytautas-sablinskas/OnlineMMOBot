from Constants.WebsitePaths import WebsitePaths
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Constants.Expressions import Expressions

class PageNavigator:
    def go_to_travel_page(chrome_handler, element_handler):
        travel_page_link = WebsitePaths.TRAVEL_PAGE.value
        travel_page_condition = EC.visibility_of_any_elements_located
        travel_page_locator = By.XPATH
        travel_page_expression = Expressions.TAKE_STEP_BUTTON.value
        chrome_handler.go_to_page(travel_page_link, element_handler, travel_page_condition, travel_page_locator, travel_page_expression)

    def go_to_battle_arena_page(chrome_handler, element_handler):
        #to implement for battle arena.
        pass

    def go_to_unfinished_questions_page(chrome_handler, element_handler):
        #to implement
        pass