from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
#here in these you write the own xpath in these code

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/")
#
driver.implicitly_wait(20)
# a = driver.find_element(By.LINK_TEXT,"Digital downloads ")
# driver.implicitly_wait(10)
# a.click()
# print(a.is_enabled())
# time.sleep(5)

#finding total no of links present in the youtube homepage
a=driver.find_elements(By.TAG_NAME,"yt-formatted-string")
print(f"Total no of links:{len(a)}")

#printing all the linksname
for i in a:
    print(i.text)

#if you get empty text which menas the link is there but text is not available.