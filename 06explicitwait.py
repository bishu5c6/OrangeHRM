from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
mywait = WebDriverWait(driver, 20, ignored_exceptions=[NoSuchElementException,
                                                       ElementNotVisibleException,
                                                       ElementNotSelectableException, Exception])#explicit wait declaration


driver.maximize_window()
driver.get('https://www.google.com/')
search = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
search.send_keys("selenium")
time.sleep(2)
search.submit()

driver.implicitly_wait(20)
mywait.until(EC.presence_of_element_located((By.TAG_NAME,"h3"))).click()#ec is expected condidtion
time.sleep(5)
