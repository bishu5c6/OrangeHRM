from selenium.webdriver.common.by import By
from selenium import webdriver
import  time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.save_screenshot("E:\OrangeHRM\homaepage.png")
# driver.save_screenshot(os.getcwd()+"\homepage11.png")
driver.get_screenshot_as_file(os.getcwd()+"\homepage11.png")
driver.get_screenshot_as_base64()
driver.get_screenshot_as_png()




time.sleep(2)