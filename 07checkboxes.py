from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
#here in these you write the own xpath in these code

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# checkbox = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(8) > div:nth-child(3)")
# checkbox.click

mcheckboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(f"len of the checkboxes is: {len(mcheckboxes)}")

# for i in mcheckboxes:
#     i.click()

# for i in mcheckboxes:
#     weekname = i.get_attribute('id')
#     if weekname == 'monday' or weekname=='sunday' or weekname=='thursday':
#         i.click()

#selecting only last 2 elemeents
# for i in range(len(mcheckboxes)-2,len(mcheckboxes)):
#     mcheckboxes[i].click()
# time.sleep(3)

#select first 2 checkboxes.
# for i in range(len(mcheckboxes)):
#     if i<2:
#         mcheckboxes[i].click()

#clearing all the checkboxes
for i in mcheckboxes:
    i.click()
time.sleep(5)
for i in mcheckboxes:
    if i.is_selected():
        i.click()

time.sleep(5)