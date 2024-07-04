from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker("ru_RU")

from base.base_class import Base


class Client_inform_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    first_name = '//input[@id = "first-name"]'
    last_name = '//input[@id = "last-name"]'
    postal_cod = '//input[@id = "postal-code"]'
    button_continue = '//input[@id = "continue"]'




    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_cod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_cod)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))


    # Action

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input First Name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input Last Name')

    def input_postal_cod(self, postal_cod):
        self.get_postal_cod().send_keys(postal_cod)
        print('Input Postal Cod')

    def click_button_continue(self):
        self.get_button_continue().click()
        print('Click Button Continue')


    # Methods

    def input_inform(self):
        self.get_current_url()
        self.input_first_name(fake.first_name_male())
        self.input_last_name(fake.last_name_male())
        self.input_postal_cod(fake.password())
        self.click_button_continue()









