from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
    # ordenar productos
    sorting_dropdown = driver.find_element(By.CLASS_NAME,'product_sort_container')

    select = Select(sorting_dropdown)
    
    select.select_by_value('hilo')
    
    WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"inventory_item_price"))
    )
    
    #obtener precios
    prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    prices_list = [float(price.text.replace("$","")) for price in prices]
    
    print(prices_list)
    
except NoSuchElementException:
    print("Error en el login")
finally:
    time.sleep(10)
    driver.quit()

