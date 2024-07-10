import datetime
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_page
from pages.client_inform_page import Client_inform_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_select_product():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    print('Start Test')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_inform_page(driver)
    cip.input_inform()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()


