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

url = "https://pnmi.segob.gob.mx/reporte"

driver.get(url)

dropdown_tipo = driver.find_element(By.NAME, "tipo")
dropdown_tipo.click()

tipo = Select(dropdown_tipo)
tipo.select_by_value("REVISTA")   

dropdown_estado = driver.find_element(By.NAME, "estado")
dropdown_estado.click()

estado = Select(dropdown_estado)
estado.select_by_value("9")

buscar = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')

buscar.click()

data = []

for i in range(0,4):
    nombres = driver.find_elements(By.XPATH, '//div[@class="col-md-10 resultado redireccion"]')    
    nombre = nombres[i].text

    nombres[i].click()
    municipios = driver.find_elements(By.XPATH, '//div[@class="col-md-4"]/p[2]')
    municipio = municipios[1].text
    
    pestana_circulacion = driver.find_element(By.XPATH, '//ul[@class="nav nav-tabs nav-justified navfont"]/li[4]')
    pestana_circulacion.click()
    
    circulacion = driver.find_element(By.XPATH, '//div[@id="circulacion-y-distribucion-geografica"]/div[@class="row"][3]/div[@class="col-md-12"]/p[2]')
    
    circulacion = circulacion.text
    
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)
    
    driver.refresh()
    
    try:
        Alert(driver).accept()
        time.sleep(3)
    except:
        pass    
    
    data.append({"nombre":nombre, "municipio":municipio, "circulacion":circulacion})

bd = pd.DataFrame(data)

bd.to_csv('revista.csv', index=False)