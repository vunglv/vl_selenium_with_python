from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)

element = driver.find_element(By.NAME,"username")
element.send_keys("Admin")

element = driver.find_element(By.NAME,"password")
element.send_keys("admin123")

element = driver.find_element(By.XPATH,"//button[text()=' Login ']")
element.click()
time.sleep(3)

print(driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").text)

element = driver.find_element(By.XPATH,"//span[text()='Admin']")
element.click()
time.sleep(1)

element = driver.find_element(By.CLASS_NAME,"oxd-topbar-header-breadcrumb")
assert "Admin" in element.text

driver.close()
