from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Bases


class main_page(Bases):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart= "//div[@id='shopping_cart_container']"

    # GETTERS

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

 # ACTIONS
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select_product_1")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    #METODS

    def select_product(self,):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
