from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = Options()   
options.binary_location = r'/usr/local/bin/geckodriver'
driver = webdriver.Firefox(options=options)

url = "https://conelmazodando.com.ve"

driver.get(url)

contenedores = driver.find_elements(By.XPATH, "//div[@class='contenedor4']/a")

data = []

for contenedor in contenedores:
    
    WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='contenedor4']/a"))
    )   
    link = contenedor.get_attribute("href")
    driver.get(link)
    
    driver.execute_script("window.history.go(-1)")
    
driver.close()
driver.quit()


