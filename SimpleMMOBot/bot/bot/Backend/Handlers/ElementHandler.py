from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as ex
import time
class ElementHandler:
    def __init__(self, driver):
            self.driver = driver

    def click_element(element):
        if element and element.is_enabled():
            element.click()
            time.sleep(1)

    def find_element(self, locator_type, expression_type):
        try:
            element = self.driver.find_element(locator_type, expression_type)
            return element
        except ex.NoSuchElementException:
            return None

    def wait_for_element(self, expected_condition, locator_type, expression_type):
        try:
            element = WebDriverWait(self.driver, 10).until(expected_condition((locator_type, expression_type)))
            return element
        except ex.TimeoutException:
            print("Timed out")
            return None

    def find_and_click_on_element(self, locator_type, expression_type):
        element_was_clicked = False
        element = self.find_element(locator_type, expression_type)
        element_was_found = element and element.is_enabled() and element.is_displayed()
        if element_was_found:
            try:
                element.click()
                time.sleep(1)
                element_was_clicked = True
            except:
                pass
        return element_was_clicked
    
    def wait_for_element_and_send_input(self, expected_condition, locator_type, expression_type, text):
        element = self.wait_for_element(expected_condition, locator_type, expression_type)
        element_exists = element != None
        if element_exists:
            element.send_keys(text)

