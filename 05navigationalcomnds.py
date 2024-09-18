from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get('https://snapdeal.com/')
driver.maximize_window()
time.sleep(2)
driver.get('https://www.amazon.in/a/c/r?k=DCgb5bHxlhTVHC2CWnOxRtC4m')
driver.maximize_window()
time.sleep(2)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(4)
driver.close()
