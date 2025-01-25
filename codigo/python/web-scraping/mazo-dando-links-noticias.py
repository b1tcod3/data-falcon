from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = Options()   
options.binary_location = r'/snap/bin/geckodriver'
# options.binary_location = r'/usr/local/bin/geckodriver'
driver = webdriver.Firefox(options=options)

url = "https://conelmazodando.com.ve"

driver.get(url)

# contenedores = driver.find_elements(By.XPATH, "//div[@class='contenedor4']/a")

contenedores = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='contenedor4']/a"))
    )

print(contenedores)

# links = []

# for contenedor in contenedores:
#     try:  
#         link = contenedor.get_attribute("href")
#         print(link)
#     except StaleElementReferenceException:
#         print("No se pudo obtener el enlace")
        
    # links.append({'enlace':link})
    # df = pd.DataFrame(links)
    # df.to_csv('links-mazo-dando.csv', index=False)
driver.quit()


