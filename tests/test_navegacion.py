from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_navegacion(login_in_driver):
    

    try:
        driver = login_in_driver
        assert driver.title == "Swag Labs" # comparo el titulo de la pagina con el que yo espero que tenga
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.CLASS_NAME, "product_sort_container").click()
        
    except Exception as e:
        print(f"Error en test_navegacion: {e}")
        raise #se finaliza la prueba a traves del error 
    finally:
        driver.quit() 
         

