from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
import time
import pandas as pd

options = Options()   
options.binary_location = r'/snap/bin/geckodriver'
driver = webdriver.Firefox(options=options)

url = "https://conelmazodando.com.ve"

driver.get(url)

contenedores = driver.find_elements(By.CLASS_NAME, 'contenedor4')



driver.close()
driver.quit()


