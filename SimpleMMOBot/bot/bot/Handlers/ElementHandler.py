from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as ex
import time
from Handlers.Logger import Logger

class ElementHandler:
    def __init__(self, driver):
            self.driver = driver
            self.logger = Logger()

    def find_element(self, locator_type, expression_type):
        try:
            element = self.driver.find_element(locator_type, expression_type)
            return element
        except ex.NoSuchElementException:
            self.logger.log_error("Element not found with locator type: {} and expression type: {}".format(locator_type, expression_type))
            return None

    def wait_for_element(self, expected_condition, locator_type, expression_type):
        try:
            element = WebDriverWait(self.driver, 10).until(expected_condition((locator_type, expression_type)))
            return element
        except ex.TimeoutException:
            self.logger.log_error("Timeout while waiting for element with locator type: {} and expression type: {}".format(locator_type, expression_type))
            return None

    def find_and_click_on_element(self, locator_type, expression_type):
        element = self.find_element(locator_type, expression_type)
        element_was_clicked = False
        element_was_found = element and element.is_enabled() and element.is_displayed()
        if element_was_found:
            try:
                element.click()
                time.sleep(1)
                element_was_clicked = True
            except Exception as e:
                self.logger.log_error("Failed to click on element with locator type: {} and expression type: {}. Error: {}".format(locator_type, expression_type, str(e)))

        return element_was_clicked
    
    def wait_for_element_and_send_input(self, expected_condition, locator_type, expression_type, text):
        element = self.wait_for_element(expected_condition, locator_type, expression_type)
        element_exists = element != None
        if element_exists:
            element.send_keys(text)

        