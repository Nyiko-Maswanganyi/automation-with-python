 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Actions with the keyboard
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import numpy as np
import datetime
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
 
 
 


driver = webdriver.Chrome('C:/Users/nymaswan2201/Desktop/soni/chromedriver_win32/chromedriver' )
#maximize browser
driver.maximize_window()
driver.get('https://github.com/login')

#credentials for to be used in logging in
username = "nyikotaker@gmail.com"
password = "Maswanganyi77"

driver.find_element(By.ID, 'login_field').send_keys(username)
# find password input field and insert password as well
driver.find_element(By.ID, 'password').send_keys(password)
# click login button
driver.find_element(By.NAME,'commit').click()
 
 
