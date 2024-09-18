from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")


driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']").click()


alertwindoe = driver.switch_to.alert
print(alertwindoe.text)
alertwindoe.send_keys("MY name is P>B>Y")
# alertwindoe.accept() #in order to submit
alertwindoe.dismiss() #in order to dismiss
time.sleep(5)