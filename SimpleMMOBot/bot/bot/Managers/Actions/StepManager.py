from Handlers.TimeHandler import TimeHandler
from Managers.Files.FileManager import FileManager

class StepManager:
    def take_steps(take_step_button):
        TimeHandler.sleep_for_random_time(0.1, 1.6)
        if take_step_button.is_enabled():
            FileManager.update_bot_current_action(status_text="Taking steps")
            take_step_button.click()