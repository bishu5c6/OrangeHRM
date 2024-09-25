from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import  time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(15)
# cookies = driver.get_cookies()
# print(f"size of cookies are: {len(cookies)}")
# for i in cookies:
#     print(i)#print all the cookies
#     print()
#     print(i.get('name'),":",i.get('value'),i.get('expirydate'))

#add a new cookie
#when you add cookies you must to have to add value otherwise it will throw error
driver.add_cookie({"name":"bishu", "status":"added","value":"123456"})
cookies = driver.get_cookies()
print(f"size of cookies are after afding new : {len(cookies)}")

#delete specific cookie from the browser.
driver.delete_cookie("bishu")#mention name of the cookie
cookies = driver.get_cookies()
print(f"size of cookies are after deletion : {len(cookies)}")