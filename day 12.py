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
import os
location = os.getcwd()
driver = webdriver.Chrome()
#options = webdriver.EdgeOptions()    #edge browse
# driver = webdriver.Firefox()    #firefox

# --------------------------------------------------------------------------------------------------------------
# keyword Actions
# ( ctrl+a , ctrl+c , tab , ctrl+v ) key operations

# url = "https://text-compare.com/"
# url = "https://file-examples.com/index.php/sample-documents-download/sample-doc-download/"
# url = "https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/"
url = "https://www.sitepoint.com/mime-types-complete-list/"
driver.get(url)
# ---------------------------------------------------------------------------------
# edge_run
# Optional: Set Edge options if needed
# service = service.Service(r'E:\edge drive\msedgedriver.exe')  # Replace with your Edge driver path
# driver = webdriver.Edge(service=service, options=options)
# # url = "https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/"
# url = "https://file-examples.com/index.php/sample-documents-download/sample-doc-download/"
# driver.get(url)
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()  #document
# # driver_path = r"C:\Users\JAI-SHANKAR\Downloads\edge drive\msedgedriver.exe"
# service = Service(executable_path=driver_path)
# driver = webdriver.Edge(service=service)
# ----------------------------------------------------------------------------------
# firefox
# options = Options()
# options.executable_path = "C:\\Users\\JAI-SHANKAR\\Downloads\\firefox\\geckodriver.exe"
# url = "https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/"
# driver.get(url)
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//body[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/a[1]").click()
# ---------------------------------------------------------------------------------
driver.maximize_window()
# --------------------------------------------------------------------------------------------------------------------
# KEYBOARD ACTION FOR COPY AND PASTE

# input1 = driver.find_element(By.ID,"inputText1")
# input2 = driver.find_element(By.ID,"inputText2")
# input1.send_keys("welcome jai tester page")
#
# act = ActionChains(driver)
#
# # input1 box
#
# # ctrl a select the box
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
#
# # ctrl c copy the element
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()
#
# # press tab to next box
# act.send_keys(Keys.TAB).perform()
#
# # press ctrl v to paste the element
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
#
# driver.find_element(By.XPATH,"//div[@class='compareButtonText']").click()
# ----------------------------------------------------------------------------------------------------------------

# HOW TO DOWNLOAD FILE USING AUTOMATION

def chrome_setup():
    # download file in desire location
    driver.implicitly_wait(10)
    #preferences={"download.default_directory":location,"plugins.always_open_pdf_externally": True}
    preferences = {"download.default_directory": location}
    return driver
# my_drive = chrome_setup()

def edge_setup():
    # preferences = {"download.default_directory": location,"plugins.always_open_pdf_externally": True}
    preferences = {"download.default_directory": location}
    return driver


# driver.find_element(By.XPATH,"//body[1]/div[1]/main[1]/section[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/a[1]").click()
time.sleep(5)


# -----------------------------------------------------------------------------------------------------------

# mime type




