from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

email = driver.find_element(By.CSS_SELECTOR,"#Email")
email.clear()
email.send_keys("123@gmail.com")
time.sleep(2)
print("result of text is", email.text)
print('resultof get attribute is', email.get_attribute('value'))
button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")

print(button.text)
print(button.get_attribute('type'))