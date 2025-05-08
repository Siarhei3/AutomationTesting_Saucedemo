from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Bases


class payment_page(Bases):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    finish_button = "//button[@id='finish']"


    # GETTERS

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

 # ACTIONS
    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish_button")

    #METODS

    def payment(self,):
        self.get_current_url()
        self.click_finish_button()
