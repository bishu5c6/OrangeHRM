from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  time
import requests
#here in these you write the own xpath in these code

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://deadlinkcity.com/")
driver.implicitly_wait(20)
#driver.find_element(By.CSS_SELECTOR,"Don't use it in blank tab, open google.com").submit()
time.sleep(5)
all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"total no of links present: {len(all_links)}")

count = 0
for links in all_links:
    url = links.get_attribute("href")
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code>=400:
        print(url, "is a broken link")
        count+=1
    else:
        print(url, "is a valid link")

print("Total no of broken links are: ",count)