from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

time.sleep(4)
# driver.close()
driver.quit()
time.sleep(5)