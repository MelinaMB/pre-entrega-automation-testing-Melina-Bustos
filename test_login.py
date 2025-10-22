from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_loging():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # es dinamico te hace esperar como maximo 5 segundos entre cada accion y accion


    try:
    # login
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    #Validacion de la redireccion de la pagina

        assert '/inventory.html' in driver.current_url

    

        print("TEST OK")

    finally:
        driver.quit()
