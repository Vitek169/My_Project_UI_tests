from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    user_name = '//input[@id = "user-name"]'
    password = '//input[@id = "password"]'
    button_login = '//input[@id = "login-button"]'
    main_word = '//span[@class="title"]'


    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Action

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input Username')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input Password')

    def click_login_button(self):
        self.get_button_login().click()
        print('Click Button Login')


    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'Products')









