from selenium import webdriver
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

driver = webdriver.Chrome()
url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
driver.get(url)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[normalize-space()='Click here to enter your code']").click()
driver.find_element(By.XPATH,"//input[@id='coupon_code']").send_keys("JAI0021")
driver.find_element(By.XPATH,"//button[normalize-space()='Apply coupon']").click()
driver.find_element(By.XPATH,"(//input[@id='product_551'])[1]").click()
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("SRI JAYA")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("shankar")
driver.find_element(By.XPATH,"//textarea[@id='order_comments']").send_keys("onum ela")
driver.find_element(By.XPATH,"//input[@id='dob']").click()
date_pic_mon=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
date_pic_mon.select_by_visible_text("Dec")
date_pic_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
date_pic_year.select_by_visible_text("2003")
date = driver.find_element(By.XPATH,"//a[normalize-space()='10']")
date.click()
driver.find_element(By.XPATH,"//input[@id='sex_1']").click()
driver.find_element(By.XPATH,"//input[@id='addmorepax']").click()
driver.find_element(By.XPATH,"//span[@id='select2-addpaxno-container']").click()
passenger = driver.find_elements(By.XPATH,"//span[@class='select2-results']/ul/li")
for passengers in passenger:
    if passengers.text=="add 1 more passenger (100%)":
        passengers.click()
        break
driver.find_element(By.XPATH,"//input[@id='traveltype_2']").click()
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("mdu")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("chennai")
date_pic_mont = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
date_pic_mont.select_by_visible_text("Jul")
date_pic_yea = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
date_pic_yea.select_by_visible_text("2023")
dat = driver.find_element(By.XPATH,"//a[normalize-space()='10']")
dat.click()

time.sleep(5)