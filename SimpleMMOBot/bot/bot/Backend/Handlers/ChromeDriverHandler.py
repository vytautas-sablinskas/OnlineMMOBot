from Handlers.FileHandler import FileHandler
from Constants.FilePaths import FilePaths
from Constants.WebsitePaths import WebsitePaths
from selenium_profiles.webdriver import Chrome
from selenium_profiles.profiles import profiles
from selenium.webdriver import ChromeOptions

class ChromeDriverHandler:
    def __init__(self):
        self.driver = self.start_driver()

    def add_arguments(self, options, arguments):
        no_arguments_to_add = not arguments
        if no_arguments_to_add:
            return

        for argument in arguments:
            options.add_argument(argument)

    def start_driver(self):
        profile = profiles.Windows()
        options = ChromeOptions()

        options.add_argument('--auto-open-devtools-for-tabs')
        chrome_driver_arguments = FileHandler.get_array_from_file(FilePaths.CHROME_ARGUMENTS.value, delimiter='\n')
        self.add_arguments(options, chrome_driver_arguments)
        
        driver = Chrome(profile, options=options, uc_driver=False)
        driver.start_client()
        driver.get(WebsitePaths.LOGIN_PAGE.value)

        return driver
    
    def go_to_page(self, location, element_handler, expected_condition, locator_type, expression_type):
        self.driver.get(location)
        element_handler.wait_for_element(expected_condition, locator_type, expression_type)