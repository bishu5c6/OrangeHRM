from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mypage.rediff.com/login/dologin")

driver.find_element(By.CSS_SELECTOR,"input[value='Login']").click()
alertwindow = driver.switch_to.alert
alertwindow.accept()
time.sleep(5)