import pytest
from selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_opt = Options() #abre chrome como incognito y desactiva popup de contraseña filtrada 
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options = chrome_opt)
    yield driver # se utiliza para los fixture en pytest para devolver un valor al test
                # despues de que el test termina continua ejecutando el test que viene
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver