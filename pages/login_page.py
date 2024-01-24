from utils.locators import *
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)
        
    def login(self, user, password):
        self.find_element(*self.locator.txt_user).send_keys(user)
        self.find_element(*self.locator.txt_password).send_keys(password)
        self.find_element(*self.locator.btn_login).click()