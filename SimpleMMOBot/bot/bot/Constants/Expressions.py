from enum import Enum


class Expressions(Enum):
    EMAIL_INPUT = "email"
    PASSWORD_INPUT = "password"
    LOGIN_BUTTON = "button[type='submit']"

    PRESS_VERIFY_BUTTON = "Press here to verify"
    CONFIRM_EXISTENCE_BUTTON = "Press here to confirm your existence"
    TAKE_STEP_BUTTON = "//button[contains(text(), 'Take a step')]"
    GATHER_BUTTON = "crafting_button"
    

