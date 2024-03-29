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

# mouse operation
#
# actionchain
# 1 mouse hover - move_to_element(element)
# 2 right click - context_click(element)
# 3 double click - double_click(element)
# 4 drag and drop - drag_and_drop(source,target)
# 5 range slider - drag and drop by offset(element,x,y)
# 6 scrolling page

# Date picker
# ---------------
# 1 standard
# 2 non-standard(customized)
# url = "https://jqueryui.com/datepicker/"
# url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# url = "https://api.jquery.com/contextmenu/"
url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3"
url ="http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
url = "https://jqueryui.com/resources/demos/slider/range.html"
url = "https://www.worldometers.info/geography/flags-of-the-world/"
driver.get(url)
driver.maximize_window()
# --------------------------------------------------------------------------------------------------------------

# username_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
# username_field.send_keys("Admin")
#
# username_field = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
# )
# username_field.send_keys("Admin")
#
# username_pass = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
# )
# username_pass.send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
#
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()
#
# # act = ActionChains(driver)
# # act.move_to_element(admin).move_to_element(use).click().perform()
#
# time.sleep(4)
# -------------------------------------------------------------------------------------------------------------

# # right click
# driver.implicitly_wait(10)
# inner = driver.find_element(By.XPATH,"//div[@class='demo code-demo']//iframe")
# driver.switch_to.frame(inner)
# actt = driver.find_element(By.XPATH,"//body//div")
#
# act = ActionChains(driver)
# act.context_click(actt).perform()
#
# time.sleep(4)
# ------------------------------------------------------------------------------------------------------------------

# double click

# inner = driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
# driver.switch_to.frame(inner)
# field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
# field1.click()
# field1.send_keys("welcome")
#
# button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
# act = ActionChains(driver)
# act.double_click(button).perform()

# ----------------------------------------------------------------------------------------------------------------------

# drag and drop

# driver.implicitly_wait(10)
# source = driver.find_element(By.ID,"box6")
# target = driver.find_element(By.ID,"box106")
# act = ActionChains(driver)
# act.drag_and_drop(source, target).perform()   #perform drag and drop perform

# -----------------------------------------------------------------------------------------------------------------------

# range slider

# min = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
# max = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
#
# print("location of before move",min.location) #{'x': 202, 'y': 46}
# print("location of max slider",max.location) #{'x': 808, 'y': 46}
#
# act = ActionChains(driver)
# act.drag_and_drop_by_offset(min,100,0).perform()
# act.drag_and_drop_by_offset(max,-100,0).perform()
#
# print("location of after move",min.location)
# print("location of max slider",max.location)

# --------------------------------------------------------------------------------------------------------------------

# scroller by using javascript scripts

# 1. scroll down by pixel
driver.execute_script("window.scrollBy(0,3000)","")
value = driver.execute_script("return window.pageYOffset;")
print("the num of value moved :",value) # 3000

# scroll till the element is visible
flag = driver.find_element(By.XPATH,"//img[@src='/img/flags/small/tn_in-flag.gif']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print("The num of value moved :",value) # 4588

# scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("The num of value moved to end of page :",value) # 11393

# scroll to initial position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("The num of value return to initial value :",value)

# ---------------------------------------------------------------------------------------------------------


