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

#it ignore the notification it,just disable the pop up,s
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-notificstion")
#driver = webdriver.Chrome(options=options)
#url ="https://whatmylocation.com/"
# driver.get(url)
# driver.maximize_window()
driver = webdriver.Chrome()


#WEB TABLE (STATIC TABLE , DYNAMIC TABLE)

#STATIC TABLE
url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.maximize_window()

#count num of row and column
#read specific row and column data
#read all the row & column data
#read data based on condition(list books name those author is mukesh)

#numm row and column
noofrows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noofcolumns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(noofrows)
print(noofcolumns)

#read specific row and columndr
mast = driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr[5]/td[1]").text
print(mast)

#read all row and coliumn
for r in range(2,noofrows+1):
    for c in range(1,noofcolumns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='')
    print()

#read data based on condition

for r in range(2,noofrows+1):
    auth = driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr["+str(r)+"]/td[2]").text
    if auth=="Mukesh":
       book =  driver.find_element(By.XPATH, "//table[@name='BookTable']//tbody/tr[" + str(r)+"]/td[2]").text
    print(book,"",auth)


