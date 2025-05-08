from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Bases


class cart_page(Bases):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    checkout_button = "//button[@id='checkout']"


    # GETTERS

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

 # ACTIONS
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout_button")

    #METODS

    def product_confirmation(self,):
        self.get_current_url()
        self.click_checkout_button()
