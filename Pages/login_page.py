from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Bases


class login_page(Bases):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    user_name = "//*[@id='user-name']"
    password = "//*[@id='password']"
    button_login = "//*[@id='login-button']"
    main_world = "//span[@class='title']"

    # GETTERS

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_world(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_world)))



    # ACTIONS

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click button login")

    #METODS

    def autorithation(self,):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_button_login()
        self.assert_world(self.get_main_world(), 'Products')