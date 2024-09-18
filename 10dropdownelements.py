from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.implicitly_wait(20)
element = Select(driver.find_element(By.ID,"dropdown"))

# select = Select(element)
#
# select.select_by_visible_text("India")
# select.select_by_value("10")#capture from html
# select.select_by_index("2")#count from ourseleves from options starts with 0
#
# option_count = len(select.options)
# expected_count = 3
# if option_count == expected_count:
#     print("apss")
# else:
#     print("fail")
# time.sleep(3)

#or
alloptions = element.options
print("Total no of options: ", len(alloptions))

for opt in alloptions:
    print(opt.text)#gives all the text

#select the dropdown options without using any built in functions.
for opt in alloptions:
    if opt.text  == "Option 1":
        opt.click()
        break
time.sleep(3)

