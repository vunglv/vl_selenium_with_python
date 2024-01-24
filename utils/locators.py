from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    txt_user = (By.NAME,'username')
    txt_password = (By.NAME,'password')
    btn_login = (By.XPATH,"//button[text()=' Login ']")

class HomPageLocators(object):
    btn_user_name = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    menu_left_admin = (By.XPATH,"//span[text()='Admin']")
    title_page_admin = (By.CLASS_NAME,"oxd-topbar-header-breadcrumb")
