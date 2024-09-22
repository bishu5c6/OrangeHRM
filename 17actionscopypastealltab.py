from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()

firstinputbox = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
secondinputbox = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

firstinputbox.send_keys("MY NAME IS P.BISWANTH")

act = ActionChains(driver)
#ctrl + a we are writing the code.

act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

#if you want to write in a single line

#now we eill try to copy the statement
act.key_down(Keys.CONTROL)#if you want to  press fist you have to key_down
act.send_keys("c")
act.key_up(Keys.CONTROL)#helps in releasing the control key
act.perform()

act.key_down(Keys.TAB)#if you want to  press fist you have to key_down
act.perform()

act.key_down(Keys.CONTROL)#if you want to  press fist you have to key_down
act.send_keys("v")
act.key_up(Keys.CONTROL)#helps in releasing the control key
act.perform()

time.sleep(5)