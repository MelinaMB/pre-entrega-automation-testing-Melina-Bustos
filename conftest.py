import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver # se utiliza para los fixture en pytest para devolver un valor al test
                # despues de que el test termina continua ejecutando el test que viene
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver