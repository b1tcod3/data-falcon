from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()   
options.headless = True
options.binary_location = r'/snap/bin/geckodriver'
driver = webdriver.Firefox(options=options)

driver.get('https://duckduckgo.com/')
search_form = driver.find_element(By.ID, 'searchbox_input')
search_form.send_keys('Web scraping')
search_form.submit()

results = driver.find_elements(By.CLASS_NAME, 'react-results--main')

driver.close()
driver.quit()

