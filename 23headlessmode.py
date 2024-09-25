from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument('--headless=new')
    driver = webdriver.Chrome(options=ops)
    return driver


driver = headless_chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.close()