from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Bases


class client_information_page(Bases):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    zip_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    # GETTERS

    def get_first_name (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name )))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # ACTIONS

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input zip_code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue_button")

    #METODS

    def input_information(self,):
        self.get_current_url()
        self.input_first_name("jack")
        self.input_last_name("born")
        self.input_zip_code("208778")
        self.click_continue_button()