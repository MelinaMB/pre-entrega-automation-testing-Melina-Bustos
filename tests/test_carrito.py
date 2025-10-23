from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito(login_in_driver):
    
    try:
        driver = login_in_driver
        #interacciones
       
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        productos[0].find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(5)

        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == "1", "El carrito no se actualizo correctamente"

        
    finally:
        driver.quit()