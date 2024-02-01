from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        #self.timeout = 30
        
    def open_url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    # def find_element(self, *locator):
    #     return self.driver.find_element(*locator)
    
    def find_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()
        return self.driver.find_element(*locator)