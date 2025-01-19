from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv  
import time
import os

load_dotenv()

options = Options()   
options.binary_location = r'/snap/bin/geckodriver'
driver = webdriver.Firefox(options=options)

username = "b1tcod3"
password = os.getenv('PASS')
cuenta_objetivo = "b1tcod3"

try:
    driver.get("https://www.instagram.com/accounts/login/")
    #esperar a que cargue la pagina
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click() 
    
    time.sleep(5)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'verificationCode'))
        )   
        verification_code = input("Introduce el código de verificación")
        driver.find_element(By.NAME,"verificationCode").send_keys(verification_code)
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(5)
    except Exception as e:
        print("No se necesita código de verificación",e)
    
    print("Login exitoso")
    driver.get("https://www.instagram.com/"+cuenta_objetivo)
    
    #esperar a que cargue la pagina
    time.sleep(5)
    
    publicaciones = driver.find_elements(By.XPATH,'//div[@class="x1lliihq x1n2onr6 xh8yej3 x4gyw5p x1ntc13c x9i3mqj x11i5rnm x2pgyrj"]/a')   
    
    for publicacion in publicaciones:
        enlace = publicacion.get_attribute("href")
        print(enlace)
    
finally:
    driver.quit()
    




