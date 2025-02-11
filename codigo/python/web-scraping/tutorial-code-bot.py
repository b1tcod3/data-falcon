from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()   
options.binary_location = r'/snap/bin/geckodriver'
driver = webdriver.Firefox(options=options)
user = "standard_user"
password = "secret_sauce"

url= "https://www.saucedemo.com/"

driver.get(url)

time.sleep(5)

# login
driver.find_element(By.ID, "user-name").send_keys(user)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

# chequear si esta logueado
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )    
    # agregar producto al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # iniciar el checkout
    driver.find_element(By.ID, "checkout").click()
    
    # completar el checkout
    nombre = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    
    nombre.send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("1234")
    driver.find_element(By.ID, "continue").click()
    
    # finalizar el checkout
    finalizar_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    
    finalizar_btn.click()
    
    # chequear si se finalizo la compra
    confirmacion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    print(confirmacion.text)
    
except NoSuchElementException:
    print("Error en el login")
finally:
    time.sleep(10)
    driver.quit()

