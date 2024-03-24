from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
#url = "https://testautomationpractice.blogspot.com/"
#url = "https://jaishankar.vercel.app/"
#url = "https://demo.nopcommerce.com/"
#url = "http://www.deadlinkcity.com/"
url = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"
driver.get(url)
driver.maximize_window()

#select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

#select all checkbox
# checkboxs = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# print(len(checkboxs))

#approach 1
# for i in range(len(checkboxs)):
#     checkboxs[i].click()
# time.sleep(7)

# #approch 2
# for chck in checkboxs:
#      chck.click()
# time.sleep(7)

# #select multiple chechboxs by choice
# for chck in checkboxs:
#     weekname = chck.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         chck.click()
# time.sleep(2)

#select last 2 checkbox
# #total num of element - 2=starting index
# for i in range(len(checkboxs)-2,len(checkboxs)):   #range(5,7)
#     checkboxs[i].click()

#select first 2 element
# for i in range(len(checkboxs)):
#     if i<2:
#         checkboxs[i].click()
# time.sleep(6)

# #clear all the check box
# for chck in checkboxs:
#     if chck.is_selected():
#         chck.click()
# time.sleep(5)

# # links 1 internel , 2 external , 3 broken link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# #time.sleep(4)
#
# #find total num of link in page   by tag name
# link = driver.find_elements(By.TAG_NAME,"a")
# print("Total num of links by tag name",len(link))
#
# #find total num of link in page   by Xpath
# link = driver.find_elements(By.XPATH,"//a")
# print("Total num of links by Xpath",len(link))
#
# #print all the link names
# for links in link:
#     print(links.text)

# #Broken links  find how many broken links
# allink = driver.find_elements(By.TAG_NAME,"a")
# count=0
# for link in allink:
#     url=link.get_attribute('href')
#     try:
#         res=requests.head(url)
#     except:
#         None
#     if res.status_code>=400:
#         print(url,"is broken")
#         count+=1
#     else:
#         print(url,"is valid link")
# print("Total num a fbroken links",count)

#dropdown
# driver.implicitly_wait(10)
# drop_ele = (driver.find_element(By.XPATH," //div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))
#
# #select option from object
# drop_ele.select_by_visible_text("India")


#
# def select_country(driver, country_name):
#     """Selects the specified country from the dropdown element."""
#
#     try:
#         # Improved XPath using variable (assuming ID is correct)
#         country_dropdown_xpath = f"//select[@id='input-country']"
#         wait = WebDriverWait(driver, 10)  # Wait for 10 seconds at most
#
#         # Wait for the element to be present and visible
#         drop_ele = wait.until(EC.visibility_of_element_located((By.XPATH, f"//select[@id='input-country']")))
#         select_obj = Select(drop_ele)
#
#         # Select the country by visible text
#
#         select_obj.select_by_visible_text("India")
#
#     except NoSuchElementException:
#         print("Error: Could not locate country dropdown element.")


def select_country(driver, country_name):
    """Selects the specified country from the dropdown element.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        country_name (str): The name of the country to select.
    """

   # try:
        # Consider simplifying the XPath based on your HTML structure
        #wait = WebDriverWait(driver, 10)  # Adjust wait time as needed
        country_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")))  # Replace with your accurate XPath
        select_obj = Select(country_dropdown)
        select_obj.select_by_visible_text("Albania")
        select_obj.select_by_value("10")
        select_obj.select_by_index(13)
        alloptions=country_dropdown.options

    #except NoSuchElementException:
        print("Error: Could not locate country dropdown element.")
        print("total num of option :",len(alloptions))

