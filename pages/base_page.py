
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        #self.timeout = 30
        
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    