from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get("https://www.saucedemo.com/") #ingreso a la pagina que quiero hacer las pruebas
    print("Titulo:",driver.title)
    assert driver.title == "Swag Labs" # comparo el titulo de la pagina con el que yo espero que tenga
    time.sleep(2) #dejar un tiempo para poder ver todo lo que ocurre

    print("TEST OK")
    
finally:
    driver.quit()

