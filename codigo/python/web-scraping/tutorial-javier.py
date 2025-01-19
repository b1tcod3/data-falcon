from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()   
options.add_argument("--headless")
options.binary_location = r'/snap/bin/geckodriver'
driver = webdriver.Firefox(options=options)
user = "standard_user"
password = "secret_sauce"

url= "https://www.saucedemo.com/"

driver.get(url)

time.sleep(5)

# login
drive.find_element(By.ID, "user-name").send_keys(user)
drive.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

# compras

button_1 = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")

button_1.click()

time.sleep(10)
driver.quit()

