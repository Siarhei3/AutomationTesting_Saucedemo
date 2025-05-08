from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Bases


class finish_page(Bases):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    # GETTERS
    # ACTIONS
    #METODS

    def finish(self,):
        self.get_current_url()
        self.get_screenshot()
