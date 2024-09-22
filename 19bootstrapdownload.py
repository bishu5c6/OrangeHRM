from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.implicitly_wait(10)
#finding the element
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
#caoturing all the elements from the browser
countrieslist = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrieslist))
for country in countrieslist:
    if country.text=="Hungary":
        country.click()
        break
time.sleep(5)