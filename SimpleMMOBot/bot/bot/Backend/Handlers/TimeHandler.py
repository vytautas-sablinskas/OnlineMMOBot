import time
import datetime
import random

class TimeHandler:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def sleep_for_random_time(start_seconds, end_seconds):
        sleep_time = random.uniform(start_seconds, end_seconds)
        time.sleep(sleep_time)

    def get_current_datetime():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time

    def start_timer(self):
        self.start_time = time.time()

    def elapsed_time(self):
        return self.start_time - time.time()

    def reset_timer(self):
        self.start_time = None