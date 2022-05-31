from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# ToDo 1. open site
ser = Service(r"C:\Development\chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=options)
driver.get("https://elgoog.im/t-rex/")

driver.close()



# ToDo 2. get item distance

# ToDo 3. if at distance x, jump
