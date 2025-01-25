from selenium import webdriver
from selenium.webdriver.firefox.options import Options 

options = Options()   
options.binary_location = r'/usr/local/bin/geckodriver'
driver = webdriver.Firefox(options=options)

driver.get("http://www.python.org")

print(driver.title)
driver.quit()
