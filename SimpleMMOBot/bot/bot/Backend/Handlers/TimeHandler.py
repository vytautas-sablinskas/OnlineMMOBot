import time
import datetime
import random

class TimeHandler:
    def __init__(self):
        self.start_time = time.time()

    def reset_timer(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        self.end_time = time.time()
        return self.end_time - self.start_time 
    
    def sleep_for_random_time(start_seconds, end_seconds):
        sleep_time = random.uniform(start_seconds, end_seconds)
        time.sleep(sleep_time)

    def get_current_datetime():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time    
