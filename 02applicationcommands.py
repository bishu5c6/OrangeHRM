from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

c = driver.current_url #to get the current url of the browser

print(f"the current url of the browser is: {c}")

d = driver.title
print(f"the current title of the page is: {d}")

e = driver.page_source
print(f"the page sourcee is: {e}")

