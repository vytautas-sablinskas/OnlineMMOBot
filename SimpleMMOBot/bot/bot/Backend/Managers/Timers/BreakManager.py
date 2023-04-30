from Handlers.TimeHandler import TimeHandler
from Managers.Files.FileManager import FileManager

class BreakManager:
    def __init__(self, playtime_in_minutes):
        self.timer = TimeHandler()
        self.playtime_in_minutes = playtime_in_minutes
        
    def check_break_time(self):
        no_breaks = self.playtime_in_minutes == 0
        if no_breaks:
            return False

        elapsed_time = self.timer.get_elapsed_time()
        if elapsed_time >= self.playtime_in_minutes * 60:
            return True
        
        return False
    
    def wait_until_break_time_ends(self):
        FileManager.update_bot_status("Bot is sleeping")
        print("Bot is sleeping")
        lowest_time_seconds = 2 * 60
        highest_time_seconds = 5 * 60
        TimeHandler.sleep_for_random_time(lowest_time_seconds, highest_time_seconds)
        self.timer.reset_timer()