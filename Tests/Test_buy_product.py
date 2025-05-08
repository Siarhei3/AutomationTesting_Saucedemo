from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.client_information_page import client_information_page
from Pages.finish_page import finish_page
from Pages.login_page import login_page
from Pages.main_page import main_page
from Pages.cart_page import cart_page
from Pages.payment_page import payment_page


def test_buy_product():
    options = Options()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)

    print("start test")

    login = login_page(driver)
    login.autorithation()

    mp = main_page(driver)
    mp.select_product()

    cp = cart_page(driver)
    cp.click_checkout_button()

    cip = client_information_page(driver)
    cip.input_information()

    p = payment_page(driver)
    p.click_finish_button()
    f = finish_page
    f.finish()

    driver.quit()



