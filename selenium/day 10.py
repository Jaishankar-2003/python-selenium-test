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
url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
driver.get(url)
driver.maximize_window()

# driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("12/10/2003")

# year = "2003"
# month = "December"
# date = "10"
# driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
#
# while True:
#     mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text   #month
#     yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text  #year
#     dat = driver.find_element(By.XPATH,"//a[normalize-space()='10']").text  #date
#
#     if mon==month and yr==year and dat==date:
#         break;
#     else:
#         driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()   #next arrow


driver.find_element(By.XPATH,"//input[@id='dob']").click()
#driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
date_pick_mon=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
date_pick_mon.select_by_visible_text("Dec")
date_pick_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
date_pick_year.select_by_visible_text("2023")
date=driver.find_elements(By.XPATH,"//select[@aria-label='Select year']//table/tbody/tr/td/a")
for dat in date:
    if date.text=="25":
        date.click()
        break

#assignment  https://www.dummyticket.com/dummy-ticket-for-visa-application/     interact with the application

time.sleep(3)


