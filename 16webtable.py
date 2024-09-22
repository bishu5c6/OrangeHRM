#here we are doimg the following operations
#count no of rows and cloumsn
#read specidic row and cloumn data
#read all rows and cloumn data
#read data based on conditions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#count no of rows and cloumns
rows = driver.find_elements(By.TAG_NAME,'tr')
print(f"Total no of present in the page are: {len(rows)}")

colss = driver.find_elements(By.TAG_NAME,'th')
print(f"Total no of columns present in the page are: {len(colss)}")

#capturing specifc colimns
data = driver.find_elements(By.XPATH,"//td[normalize-space()='Learn Java']")
print(data)