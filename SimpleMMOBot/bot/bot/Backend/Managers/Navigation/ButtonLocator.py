from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Constants.Expressions import Expressions

class ButtonLocator:
    def check_login_button_exists(element_handler):
        login_button_locator = By.CSS_SELECTOR
        login_button_expression = Expressions.LOGIN_BUTTON.value
        login_button = element_handler.find_element(
            locator_type=login_button_locator,
            expression_type=login_button_expression
        )

        return login_button

    def check_email_input_field_exists(element_handler):
        email_input_expected_condition = EC.visibility_of_element_located
        email_input_locator = By.NAME
        email_input_expression = Expressions.EMAIL_INPUT.value
        email_input_field = element_handler.wait_for_element(
            expected_condition=email_input_expected_condition,
            locator_type=email_input_locator,
            expression_type=email_input_expression
        )

        return email_input_field

    def check_password_input_field_exists(element_handler):
        password_input_expected_condition = EC.visibility_of_element_located
        password_input_locator = By.NAME
        password_input_expression = Expressions.PASSWORD_INPUT.value
        password_input_field = element_handler.wait_for_element(
            expected_condition=password_input_expected_condition,
            locator_type=password_input_locator,
            expression_type=password_input_expression
        )

        return password_input_field

    def check_battle_ended_link_exists(element_handler):
        battle_has_ended_locator = By.LINK_TEXT
        battle_has_ended_expression = Expressions.BATTLE_HAS_ENDED.value
        battle_has_ended_link = element_handler.find_element(
            locator_type=battle_has_ended_locator,
            expression_type=battle_has_ended_expression
        )

        return battle_has_ended_link
    
    def check_press_verify_button_exists(element_handler):
        verify_button_locator = By.LINK_TEXT
        verify_button_expression = Expressions.PRESS_VERIFY_BUTTON.value    
        press_verify_button = element_handler.find_element(
            locator_type=verify_button_locator,
            expression_type=verify_button_expression
        )

        return press_verify_button
    
    def check_press_gather_button_exists(element_handler):
        gather_button_locator = By.ID
        gather_button_expression = Expressions.GATHER_BUTTON.value
        gather_button = element_handler.find_element(
                locator_type=gather_button_locator, 
                expression_type=gather_button_expression
        )

        return gather_button
    
    def check_confirm_existence_button_exists(element_handler):
        confirm_existence_locator = By.LINK_TEXT
        confirm_existence_expression = Expressions.CONFIRM_EXISTENCE_BUTTON.value
        confirm_existence_button = element_handler.find_element(
                locator_type=confirm_existence_locator,
                expression_type=confirm_existence_expression
        )

        return confirm_existence_button
    
    def check_attack_mob_link_exists(element_handler):
        attack_mob_locator = By.LINK_TEXT
        attack_mob_expression = Expressions.ATTACK_MOB_PAGE_LINK.value
        attack_mob_link = element_handler.find_element(
                locator_type=attack_mob_locator,
                expression_type=attack_mob_expression
        )

        return attack_mob_link
    
    def check_click_attack_mob_button_exists(element_handler):
        attack_mob_button_locator = By.XPATH
        attack_mob_button_expression = Expressions.ATTACK_MOB_BUTTON.value

        attack_mob_button = element_handler.find_element(
            locator_type=attack_mob_button_locator,
            expression_type=attack_mob_button_expression
        )

        return attack_mob_button
    
    def check_gathering_level_too_low(element_handler):
        gathering_level_too_low_locator = By.XPATH
        gathering_level_too_low_expression = Expressions.GATHERING_LEVEL_TOO_LOW.value
        gathering_level_too_low_text = element_handler.find_element(
                locator_type=gathering_level_too_low_locator,
                expression_type=gathering_level_too_low_expression
        )

        return gathering_level_too_low_text
    
    def check_gathering_link_exists(element_handler, gathering_action):
        gathering_link_locator = By.XPATH
        gathering_link_expression = Expressions.LINK_TO_GATHERING_PAGE.value.format(gathering_action)
        gathering_link = element_handler.find_element(
                locator_type=gathering_link_locator,
                expression_type=gathering_link_expression
        )

        return gathering_link
    
    def check_take_a_step_button_exists(element_handler):
        take_a_step_locator = By.XPATH
        take_a_step_expression = Expressions.TAKE_STEP_BUTTON.value
        take_a_step_button = element_handler.find_element(
                locator_type=take_a_step_locator,
                expression_type=take_a_step_expression
        )

        return take_a_step_button
    
    def check_energy_points_span(element_handler):
        energy_points_locator = By.XPATH
        energy_points_expression = Expressions.ENERGY_POINTS.value
        energy_points_span = element_handler.find_element(
            locator_type=energy_points_locator,
            expression_type=energy_points_expression
        )

        return energy_points_span
    
    def check_question_points_span(element_handler):
        question_points_locator = By.XPATH
        question_points_expression = Expressions.QUESTION_POINTS.value
        question_points_span = element_handler.find_element(
            locator_type=question_points_locator,
            expression_type=question_points_expression
        )

        return question_points_span
    
    def check_item_found_span(element_handler):
        item_found_locator = By.XPATH
        item_found_expression = Expressions.YOU_HAVE_FOUND_AN_ITEM.value
        item_found_span = element_handler.find_element(
            locator_type=item_found_locator,
            expression_type=item_found_expression
        )

        return item_found_span
    
    def check_item_span(element_handler, rarity):
        item_locator = By.XPATH
        item_expression = Expressions.ITEM.value.format(rarity)
        item_span = element_handler.find_element(
            locator_type=item_locator,
            expression_type=item_expression
        )

        return item_span