from Handlers.FileHandler import FileHandler
from Constants.FilePaths import FilePaths
from Constants.WebsitePaths import WebsitePaths
from selenium_profiles.webdriver import Chrome
from selenium_profiles.profiles import profiles
from selenium.webdriver import ChromeOptions

class ChromeDriverHandler:
    def __init__(self):
        self.driver = self.start_driver()

    def add_arguments(self, driver, arguments):
        no_arguments_to_add = not arguments
        if no_arguments_to_add:
            return

        for argument in arguments:
            driver.options.add_argument(argument)

    def start_driver(self):
        profile = profiles.Windows()
        options = ChromeOptions()
        driver = Chrome(profile, options=options, uc_driver=False)
        chrome_driver_arguments = FileHandler.get_array_from_file(FilePaths.CHROME_ARGUMENTS.value, delimiter='\n')
        self.add_arguments(driver, chrome_driver_arguments)

        driver = driver.start()
        driver.get(WebsitePaths.LOGIN_PAGE.value)
        return driver
    
    def go_to_page(self, location, element_handler, expected_condition, locator_type, expression_type):
        self.driver.get(location)
        element_handler.wait_for_element(expected_condition, locator_type, expression_type)