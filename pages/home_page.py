from utils.locators import *
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomPageLocators
        super().__init__(driver)

    def get_user_info(self):
        user = self.find_element(*self.locator.btn_user_name).text
        print(user)

    def click_left_menu_admin(self):
         self.find_element(*self.locator.menu_left_admin).click()

    def check_page_title(self):
         title = self.find_element(*self.locator.title_page_admin).text
         return title
