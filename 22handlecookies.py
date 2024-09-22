from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import  time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

cookies = driver.get_cookies()
print(f"size of cookies are: {len(cookies)}")
# for i in cookies:
#     print(i)#print all the cookies
#     print()
#     print(i.get('name'),":",i.get('value'),i.get('expirydate'))

#add a new cookie
