from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

options = Options()   
options.binary_location = r'/snap/bin/geckodriver'
driver = webdriver.Firefox(options=options)

url = "https://www.alkosto.com/search/?text=portatil"

driver.get(url)

li_elements = driver.find_elements(By.CSS_SELECTOR, '#js-hits li')

data = []

for element in li_elements:
    try:
        data.append({
            'title': element.find_element(By.TAG_NAME, 'h3').text,  
            'price': element.find_element(By.CLASS_NAME, 'price').text, }
        )
    except NoSuchElementException:
        pass

bd = pd.DataFrame(data)

bd.to_csv('portatiles.csv', index=False)