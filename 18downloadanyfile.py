from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.select import Select
import os
location = os.getcwd()
print(location)
# different from any browser
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    preferences = {"downloads.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences) #prefs is a pre defined keyword
    driver = webdriver.Chrome()
    return driver


def edge_setup():
    preferences = {"download.default_directory":location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences) #prefs is a pre defined keyword
    driver = webdriver.Edge()
    return driver

def firefox_setup():
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox()
    return driver


driver = chrome_setup()
driver=edge_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tr[@class='even']//a[@class='btn btn-orange btn-outline btn-xl page-scroll download-button'][normalize-space()='Download sample DOC file']").click()
time.sleep(10)