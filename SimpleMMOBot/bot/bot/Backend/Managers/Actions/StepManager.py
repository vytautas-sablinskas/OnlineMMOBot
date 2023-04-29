from Handlers.TimeHandler import TimeHandler
from Managers.Navigation.ButtonClicker import ButtonClicker

class StepManager:
    def take_steps(take_step_page):
        TimeHandler.sleep_for_random_time(0.1, 1.6)
        ButtonClicker.click_button_to_new_page_and_update_status(take_step_page, "Taking steps")