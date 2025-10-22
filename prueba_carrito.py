from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    #interacciones
    productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"

    print("TEST OK")

finally:
    driver.quit()