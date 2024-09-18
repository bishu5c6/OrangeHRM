from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
# driver.find_element(By.CLASS_NAME,"checkbox").click()
search = driver.find_element(By.ID,"displayed-text")

print("enabled status",search.is_enabled())
print("diaplyed status",search.is_displayed())
print("selected status",search.is_selected())

time.sleep(5)
