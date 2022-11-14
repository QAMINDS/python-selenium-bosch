from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'

URL = 'https://qamindslab.com/'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(URL)
driver.maximize_window()
time.sleep(3)
def test_login_laboratorio():
        # Asset
        logo = driver.find_element(By.XPATH,'//img[@alt="logo"]')
        assert logo.is_displayed() , 'El logo de QA Minds no esta visible.'
        driver_wait = WebDriverWait(driver,10)
        #loader =(By.ID,'preloader')
        #driver_wait.until(ec.invisibility_of_element(loader))
        opcion_laboratorio = driver.find_element(By.XPATH,'//nav[contains(@class,"navbar-menu")]//a[text()="LABORATORIO"]')
        assert opcion_laboratorio.is_displayed() , 'La opcion de LABORATORIO no esta visible'
        
        opcion_laboratorio.click()

def teardown():
    driver.quit()

