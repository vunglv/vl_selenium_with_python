from utils.locators import *
from pages.base_page import BasePage
from testdata import users
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)
        self._wait = WebDriverWait(self.driver, 10)
        
    # def login(self, user, password):
    #     self.find_element(*self.locator.txt_user).send_keys(user)
    #     self.find_element(*self.locator.txt_password).send_keys(password)
    #     self.find_element(*self.locator.btn_login).click()

    def login(self, user):
        user = users.get_user(user)
        self.find_element(*self.locator.txt_user).send_keys(user['user_name'])
        self.find_element(*self.locator.txt_password).send_keys(user['password'])
        self.find_element(*self.locator.btn_login).click()