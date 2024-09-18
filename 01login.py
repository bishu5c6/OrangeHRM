from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
user_name = "admin"
password = "admin123"
login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(login_url)
driver.maximize_window()
driver.implicitly_wait(20)


a = driver.find_element(By.XPATH,"//input[@placeholder='Username']")
b = driver.find_element(By.NAME,"password")
driver.implicitly_wait(20)
a.send_keys(user_name)
b.send_keys(password)
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(4)
exp_title = "OrangeHRM"
act_title = driver.title
if exp_title == act_title:
    print("login is passed")
else:
    print("login is failed")