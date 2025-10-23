from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        #Validacion de la redireccion de la pagina
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"


    except Exception as e:
        print(f"Error en test_login: {e}")
        raise #se finaliza la prueba a traves del error 
    finally:
        driver.quit()

    
