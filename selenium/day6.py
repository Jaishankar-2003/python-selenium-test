from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait

# Assuming you have downloaded and set the path to the appropriate WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()
url = "https://www.google.co.in/"
driver.get(url)
driver.maximize_window()
time.sleep(7)
#wait commands
#implicit wait  , explicit wait

#implicit wait  (single statement , performance will not be reduced)
# driver.implicitly_wait(10) #it enough for all the place which will be it perform   # 10 sec is normal more then 10sec it will consider as performance bug
# driver.find_element(By.NAME,"q").send_keys("selenium")
# driver.find_element(By.NAME,"q").submit()
# driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()
# #time.sleep(60)  # 1. performance of the script is poor , 2. element is not available within the time mentioned , still chance of getting exception

#explicit wait  (more effective it nave exception handle mechanism )  disadv(multiple places,feel some difficulty)
wait = WebDriverWait(driver,10)#     poll_frequency=2,ignored_exceptions=[NoSuchElementException])
#driver.explicitly_wait(10) #work based in condition
driver.find_element(By.NAME,"q").send_keys("selenium")
driver.find_element(By.NAME,"q").submit()
driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")
wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")))
#time.sleep(6)


