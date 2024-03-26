from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests as requests
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()



#Date picker
# ---------------
# 1 standard
# 2 non-standard(customized)
#url = "https://jqueryui.com/datepicker/"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# username_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
# username_field.send_keys("Admin")

username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
)
username_field.send_keys("Admin")

username_pass = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
)
username_pass.send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

driver.implicitly_wait(10)
admin = driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
use = driver.find_element(By.XPATH,"//span[@class='oxd-topbar-body-nav-tab-item']")
# users = driver.find_element(By.XPATH,"//a[normalize-space()='Users']")

# act = ActionChains(driver)
# act.move_to_element(admin).move_to_element(use).click().perform()

time.sleep(4)




