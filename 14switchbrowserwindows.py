from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# windowid = driver.current_window_handle
# print(f"Current windowID is: {windowid}")
driver.implicitly_wait(20)

windowidnes=driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsids=driver.window_handles

# Approach1
# print(windowsids)
# parentwindoeid = windowsids[0]
# childwindowid = windowsids[1]
#
# print(f"parent windowid is: {parentwindoeid}")
# print(f"chidlwindow id is: {childwindowid}")
#
# driver.switch_to.window(childwindowid)
# print(driver.title)
#
# driver.switch_to.window(parentwindoeid)
# print(driver.title)
#approach -2
# for winid in windowsids:
#     driver.switch_to.window(winid)
#     print(driver.title)


#if you open 4 windows and want to cloase 1 ad 4 or 2and 3..
#then use the below code.
for winid in windowsids:
    driver.switch_to.window(winid)
    #mention the title of the page you want to close
    if driver.title == "OrangeHRM" or driver.title=="PUKA":
        driver.close()
    else:
        print("title not found")





time.sleep(5)
