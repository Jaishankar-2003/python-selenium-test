from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Assuming you have downloaded and set the path to the appropriate WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()
url = "https://money.rediff.com/gainers/bse/daily/groupa"
driver.get(url)
driver.maximize_window()
# xpath axes (self , parent , child , ancestor , descendant , following , following-sibling , preceding ,preceding-sibling)

#self
# test_message = driver.find_element(By.XPATH,"//a[normalize-space()='Union Bank of In']/self::a").text
# print(test_message)
# driver.find_element(By.XPATH,"//a[normalize-space()='Union Bank of In']/self::a").click()

#parent
# txt_msg = driver.find_element(By.XPATH,"//a[normalize-space()='Engineers India']/parent::td").text
# print(txt_msg)

#child
# txt_msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Engineers India']/ancestor::tr/child::td")
# print(len(txt_msg))   #5
# driver.close()

#ancestor
# txt_msg = driver.find_element(By.XPATH,"//a[normalize-space()='Engineers India']/ancestor::tr").text
# print(txt_msg)

#decendent
# txt_msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Engineers India']/ancestor::tr/descendant::*")
# print(len(txt_msg))

#following
# txt_msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Engineers India']/ancestor::tr/following::*")
# print("num of decendent",len(txt_msg)) #1328

#following-sibling
# txt_msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Engineers India']/ancestor::tr/following-sibling::*")
# print("num of decendent",len(txt_msg))  #228

#preceding
txt_msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Engineers India']/ancestor::tr/preceding::*")
print("num of decendent preced",len(txt_msg))
txt_ms = driver.find_elements(By.XPATH,"//a[normalize-space()='Engineers India']/ancestor::tr/preceding-sibling::*")
print("num of decendent presed-simb",len(txt_ms))