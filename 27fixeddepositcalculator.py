from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import  time
import os
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

file = "E:\data.xlsx"

