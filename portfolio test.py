from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
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

# driver = webdriver.Chrome()
# url = "http://127.0.0.1:5500/public_html/index.html"
# driver.get(url)
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//ul[@class='navbar-nav mr-auto']//li[2]").click()

service = Service('C:\\Users\\JAI-SHANKAR\\PycharmProjects\\testt\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigate to your webpage
driver.get("http://127.0.0.1:5500/public_html/index.html")

driver.maximize_window()
# Find the element you want to click
element = driver.find_element(By.XPATH, "//ul[@class='navbar-nav mr-auto']//li[2]")

# Create an instance of ActionChains
actions = ActionChains(driver)

# Move to the element
actions.move_to_element(element).perform()

# # Click the element
element.click()

time.sleep(4)

