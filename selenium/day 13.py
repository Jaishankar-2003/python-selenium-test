from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.edge import service
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import requests as requests
import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
import os

# driver = webdriver.Chrome()

# -----------------------------------------------------------------------------------------------------------
# bootstrap dropdown
# url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
# country = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
# #country.text
# print(len(country))
#
# for countries in country:
#     if countries.text == "India":
#         countries.click()
#         break
# -------------------------------------------------------------------------------------------------------------

# how to capture th screem shoot of the web page
# url = "https://demo.nopcommerce.com/"
# driver.get(url)
# driver.maximize_window()
# # driver.save_screenshot("C:\\Users\\JAI-SHANKAR\\PycharmProjects\\testt\\images\\homepage.png")
# # driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
# # driver.get_screenshot_as_png() # binary format
# # driver.get_screenshot_as_base64() #binary format
# -------------------------------------------------------------------------------------------------------------

# open the page in new tab  it will work ALL selenium
# url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
# driver.get(url)
# driver.find_element(By.XPATH,"//a[normalize-space()='Register']").send_keys(Keys.CONTROL+Keys.RETURN)

# ---------------------------------------------------------------------------------------------------------------

# open the 2 site in new tab it focus mainly on 2 site
# url = "https://testautomationpractice.blogspot.com/"
# driver.switch_to.new_window('tab')
# url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
# driver.get(url)

# open the site in new window
# driver.maximize_window()
# url = "https://testautomationpractice.blogspot.com/"
# driver.switch_to.new_window('window')
# url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
# driver.get(url)
# -------------------------------------------------------------------------------------------------------------------

# how to handle cookies

# url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
# driver.get(url)
# driver.maximize_window()

# capture cookies form the browser   (it contain different attribute like name time value expire date)
# cookie = driver.get_cookies()
# print(cookie)
# print("size of cookie ",len(cookie)) # 3

# print detail of all cookie (information)

# for c in cookie:
#     # print(c)
#     print(c.get('name'),":",c.get('value'))

# add new cookie to the browser
# driver.add_cookie({"name" : "MyCookie","value":"123456"})
# cookie = driver.get_cookies()
# print("size of cookie after add one",len(cookie))  # 4

# delete the specific cookie from the browser
# driver.delete_cookie({"name" : "MyCookie","value":"12345"})
# cookie = driver.get_cookies()
# print("size of cookie after delete one",len(cookie))  # 3

# delete all the cookies
# driver.delete_cookie("cookie")
# cookie = driver.get_cookies()
# print("size of cookie after delete one",len(cookie)) #3  the browser not support to delete the delete cookie it remain same

# ---------------------------------------------------------------------------------------------------------------------

# Headless mode  adv : it will run the operation on backend we can use another process , it is very fast in production   dis : we can't see the ui functionality cant analyse the functionality

# HEADLESS TEST RUN THE TEST IN BACK END
url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
chromedriver_path = "C:\\Users\\JAI-SHANKAR\\PycharmProjects\\testt\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service,options=options)

driver.get(url)
print(driver.title)
print(driver.current_url)
driver.close()

# ---------------------------------------------------------------------------------------------------------------------


