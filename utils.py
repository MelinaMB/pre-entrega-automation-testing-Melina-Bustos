import time
from selenium.webdriver.common.by import By

def login(driver):
    
    #voy a la pagina que quiero testear
    driver.get("https://www.saucedemo.com/")

    #mando las credenciales para hacer el login
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(2)
        