from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import  time
import os

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.switch_to.new_window('tab')
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# driver.find_element(By.XPATH,"//a[contains(text(),'Home')]").click()
# homelink = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH,"//a[contains(text(),'Home')]").send_keys(homelink)
#above two lines of code is available in all selenium tabs
#here in selenium 4 we have to use newtab

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.switch_to.new_window('window')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


time.sleep(5)