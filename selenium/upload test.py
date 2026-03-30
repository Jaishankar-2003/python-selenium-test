from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.options import Options
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

driver.implicitly_wait(10)
url = "https://ps.uci.edu/~franklin/doc/file_upload.html"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
driver.get(url)

# upload_element = driver.find_element(By.XPATH, "//input[@name='userfile' and @type='file']")
# upload_element.send_keys("C:\\Users\\JAI-SHANKAR\\Documents\\cert.pdf.txt")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Add Employee']").click()
raw = (driver.find_element(By.XPATH,"//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']"))
raw.click()
raw.send_keys("C:\\Users\\JAI-SHANKAR\\Pictures\\apple.png")
# raw.click()
# raw.send_keys("C:\\Users\\JAI-SHANKAR\\Pictures\\apple.png")

time.sleep(6)