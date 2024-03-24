from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests as requests
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#alert/popups (is not a web element)
# -----------------------
# alert.text
# alert.accept()
# alert.dismiss()
# authentication popup
# ---------------------
#frames/i frames


driver = webdriver.Chrome()
# url = "https://the-internet.herokuapp.com/javascript_alerts"
# driver.get(url)
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
#
#
# alertvr = driver.switch_to.alert
# print(alertvr.text)
# alertvr.send_keys("Welcome")
# alertvr.accept()    #accept is ok button , dismise is cancel button
#
# time.sleep(1)

# url = "https://mail.rediff.com/cgi-bin/login.cgi"
# driver.get(url)
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//input[@title='Sign in']").click()
# time.sleep(5)
#
# driver.switch_to.alert.accept()
#
# #driver.close()


# url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
# driver.get(url)
# driver.maximize_window()
# time.sleep(3)
# driver.back()
# time.sleep(2)


#------------------------------------------------------------------------------------------------------------------

#frames/ iframes

# url = "https://www.selenium.dev/documentation/webdriver/"
# driver.get(url)
#
# driver.find_element(By.XPATH,"//a[normalize-space()='W3C Recommendation']").click()
# driver.find_element(By.XPATH,"//body/nav[@id='toc']/ol[@class='toc']/li[6]/a[1]").click()
# driver.find_element(By.XPATH,"//section[@id='protocol']//a[@class='internalDFN'][normalize-space()='remote ends']").click()
# time.sleep(3)
#
# driver.switch_to.frame()
# #switch_to.frame(name of the frame)
# #switch_to.frame(id of the frame)
# #switch_to.frame(web element)
# #switch_to.frame(0)

# url = "https://demo.automationtesting.in/Frames.html"
# driver.get(url)
# driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
# outframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
# driver.switch_to.frame(outframe)
#
# inner = driver.find_element(By.XPATH,"//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
# driver.switch_to.frame(inner)
#
# x = driver.find_element(By.XPATH,"//input[@type='text']")
# x.send_keys("select")
#driver.switch_to.parent_frame()


#browser windows
#-------------------
# switch_to.window(windowid)
# driver.current_window_handle    window id of single browser window
# window_handles        multi window id  browser

url = "https://www.orangehrm.com/"
driver.get(url)
driver.maximize_window()

# window = driver.current_window_handle     #63A654EF0357EDF5F61E2B239A5436B3      7FC175010B0EBA1C193FA1717EDCDFC6
# print(window)
links = driver.find_elements(By.TAG_NAME, "a")

# Iterate through links and click the one with the desired href
desired_href = "/en/company/about-us/"
for link in links:
  if link.get_attribute("href") == desired_href:
    link.click()
    
# element.click()
# Click the element

# driver.explicitly_wait(10)
# element = driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM']")
# # driver.switch_to.frame(element)
# element.click()
# actions = ActionChains(driver)
#     actions.move_to_element(windo).perform()

# windo = driver.current_window_handle
# print(windo)
# windowsids = driver.window_handles

# for win in windowsids:
#     driver.switch_to.window(win)
#     print(driver.title)
# for win in windowsids:
#     driver.switch_to.window(win)
#     if driver.title=="OrangeHRM":
#         driver.close()

#
# parentwindowid = windowsids[0]
# childwindowid = windowsids[1]
#
# driver.switch_to.window(parentwindowid)
# driver.switch_to.window(childwindowid)

# print("parentwindowid")
# print("childwindowid")

time.sleep(3)

# try:
#     driver.get(url)
#     driver.maximize_window()
#
#     window_button = driver.find_element(By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[1]/a/button")
#     window_button.click()
#
#     # Wait for the new window to open
#     driver.implicitly_wait(10)  # Adjust the waiting time as needed
#
#     windowsids = driver.window_handles
#
#     if len(windowsids) >= 2:
#         parentwindowid = windowsids[0]
#         childwindowid = windowsids[0]
#
#         driver.switch_to.window(parentwindowid)
#         driver.switch_to.window(childwindowid)
#
#         print("Switched to parent window ID:", parentwindowid)
#         print("Switched to child window ID:", childwindowid)
#
#     else:
#         print("There are not enough window handles available.")
#
# except NoSuchElementException as e:
#     print("Element not found:", e)
#
# except IndexError:
#     print("IndexError: list index out of range. No child window found.")
#
# except Exception as e:
#     print("Exception occurred:", e)