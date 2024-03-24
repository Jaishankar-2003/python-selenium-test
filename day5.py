from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Assuming you have downloaded and set the path to the appropriate WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()
# url = "https://money.rediff.com/gainers/bse/daily/groupa"
#url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# url = "https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1"
# driver.get(url)
# driver.maximize_window()
# print(driver.title)     #title of the page
# print(driver.current_url)  #capture current url
# print(driver.page_source)   #source code of the page

# 1 app related  command
# 2 conditional cmd
# 3 browser cmd
# 4 navigation cmd
# 5 wait cmd

#app specifit cmd
# -------------
#get
# title
# current_url
# page_source

# conditional cmd
# is_displayed() //true false based
# is_enabled()    //if enable can do action disable no action
# is_selected()

# is_displayed() //true false based
# search = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print("display status",search.is_displayed()) #true
# print ("enable status",search.is_enabled()) #true
#
# # is_selected()
# rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
# rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")
#
# print("default",rd_male.is_selected())
# print("default",rd_female.is_selected())
#
# rd_male.click()
# rd_female.click()
#
# print("after select radio button",rd_male.is_selected())
# print(rd_female.is_selected())

#browser cmd
# close - close single browser window
# quit() - close the all browser window #interview
# driver.find_element(By.LINK_TEXT,"nopCommerce").click()
#
# time.sleep(10)
# #driver.close()
# driver.quit()


#navigation
#back
#forward
#reverse
# url = "https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1"
# driver.get(url)
# url = "https://www.snapdeal.com/"
# driver.get(url)
# driver.back()#nopcomm
# driver.forward()#snapdeal
# driver.refresh()
# time.sleep(8)
# driver.quit()

#find element vd find elements
# url = "https://demo.nopcommerce.com/register?returnUrl=%2Fregisterresult%2F1" #entire site
# driver.get(url)

url = "https://demo.nopcommerce.com/login?returnUrl=%2Fregisterresult%2F1" #login page
driver.get(url)

############   find_element - return single web element
# locator match with single web element
#element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("adragomala")
time.sleep(6)

# locator match with multiple web element
# element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text) #site map one single web element

#element not available than throw  nosuchElementException
# element = driver.find_element(By.LINK_TEXT,"Log in")
# element.click()

##########find elements()  return multi website
#locator match with single web element
# element = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(element))
# element[0].send_keys("onumpurila")
# time.sleep(6)


# #locator match with multiple web element
# element = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(element))
# #print(element[0].text)
# for ele in element:
#     print(ele.text)
# time.sleep(6)


#element not available than throw  nosuchElementException
# element = driver.find_elements(By.LINK_TEXT,"Log in")
# print(len(element))


#@@@@ text vs getattr('value') @@@@@@

email = driver.find_element(By.XPATH,"//input[@id='Email']")
email.send_keys("abc@gmail.com")
#print("result of txt ",email.text)  #txt get the inner txt written in the index
print("result of get_attribute() ",email.get_attribute('value')) #get used to print displayed word in the index return any sttribute of web elements

emailpa = driver.find_element(By.XPATH,"//input[@id='Password']")
emailpa.send_keys("yethopok")
print("element display in pass",emailpa.get_attribute('value'))

check = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("perform success login get attribute =",check.get_attribute('value'))
print("perform success login text inside =",check.text)
print("perform success login click =",check.click())

time.sleep(7)
