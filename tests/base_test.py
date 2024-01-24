import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu") 
        options.add_argument("--disable-extentions")
        options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.close()