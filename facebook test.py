from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Assuming you have downloaded and set the path to the appropriate WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()
#url = "https://www.saucedemo.com/"

#url = "https://www.facebook.com/login/"
#driver.get(url)
#driver.maximize_window()

#css selector (tag id, tag class , tag attribute , tag class attribute)
#tag id   tagname#valueofid input#email
#tag class   tagname.valueofclass
#tag attribute   tagname[attribute=value]
#tag class attribute   tagname.valueofclass[attribute=value]
#xml path html dom
#absolute/full xpath   relative/half xpath    options(  or (either 1 match true ), and (both will match then only match),,
#contains (@id,st) , [start-with(@id,'st')] , text()-> find element using innner text
#tag & id ( tagname#value of id)  input#email
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc") #it will also acceptable

#tag and class combination
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc")


#tag attribute   tagname[attribute=value]     input[placeholder=Email address or phone number]
#driver.find_element(By.CSS_SELECTOR,"input[name=email]").send_keys("abc")


#tag class attribute   tagname.valueofclass[attribute=value]
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=email]").send_keys("abc")#email
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=pass]").send_keys("abc")#password


#absolutexpath
url = "https://www.saucedemo.com/"
driver.get(url)
driver.maximize_window()

#asolute path
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("standard_user")
#driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys("secret_sauce")
#element = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")

#relative path
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("secret_sauce")
element = driver.find_element(By.XPATH,"//*[@id='login-button']")

element.click()
time.sleep(5)

# xpath axes (self , parent , child , ancestor , descendant , following , following-sibling , preceding ,preceding-sibling)

x
