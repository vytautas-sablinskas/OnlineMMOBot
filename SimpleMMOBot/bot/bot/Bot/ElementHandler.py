from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as ex
import time
import Logger

class ElementHandler:
    def __init__(self, driver, log_file_path="Logger/logs.txt"):
            self.driver = driver
            self.logger = Logger(log_file_path)

    def find_element(self, locator_type, expression_type):
        try:
            element = self.driver.find_element(locator_type, expression_type)
            return element
        except ex.NoSuchElementException:
            pass
    
        return None

    def wait_for_element(self, expected_condition, locator_type, expression_type):
        try:
            element = WebDriverWait(self.driver, 10).until(expected_condition((locator_type, expression_type)))
            return element
        except ex.TimeoutException:
            return None

    def find_and_click_on_element(self, locator_type, expression_type):
        element = self.find_element(locator_type, expression_type)
        element_was_clicked = False
        if element.is_enabled() and element.is_displayed():
            try:
                element.click()
                time.sleep(1)
                element_was_clicked = True
            except:
                pass

        return element_was_clicked
