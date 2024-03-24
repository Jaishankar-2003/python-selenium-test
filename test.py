from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Assuming you have downloaded and set the path to the appropriate WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()
#url = "https://www.saucedemo.com/"

url = "http://www.automationpractice.pl/index.php"
driver.get(url)
driver.maximize_window()
#name = driver.find_element(By.ID,"user-name")
#name.send_keys("standard_user")
#name = driver.find_element(By.ID,"password")
#name = driver.find_element(By.ID,"password")
#name.send_keys("secret_sauce")

#name = driver.find_element(By.ID,"user-name").send_keys("standard_user")
#name = driver.find_element(By.ID,"password").send_keys("secret_sauce")
#name = driver.find_element(By.ID,"login-button").click()
#name.click()
#button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
#button.click()

#locating the slides(automation practice)
slider = driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(slider))#5 pic-slides total num of slides
#anchor tag
link = driver.find_elements(By.TAG_NAME,'a')
print(len(link))# total num of links






time.sleep(5)

#locators

#id,name,linktext,partiallinktxt

#more the 1 element (class name(li,) , tagname )

# customised locator (css selector(Tag & id,class,attribute, both class,attribute) , xpath(absolute,relatuive))



