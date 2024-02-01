from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time

class TestLogin(BaseTest):
    def test_url_and_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_url()
        login_page.login('Admin')
        home_page = HomePage(self.driver)
        home_page.get_user_info()
        home_page.click_left_menu_admin()
        print(home_page.check_page_title())
        assert "Admin" in home_page.check_page_title()
        time.sleep(10)