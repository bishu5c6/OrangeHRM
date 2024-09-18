from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
driver.implicitly_wait(20)
innerframe = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(innerframe)
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("hi")

#if we you want to go from innerframe to outer frame.
driver.switch_to.parent_frame()
time.sleep(5)