from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'

URL = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)
driver.get(URL)
driver.maximize_window()

#Espera explicita
def test_progress_bar_explicit():
    boton_download = driver.find_element(By.ID,'downloadButton')
    assert boton_download.is_displayed() , 'el boton Download no se encuentra visible'
    assert boton_download.is_enabled() , 'el boton Download no se encuentra habilitado'
    boton_download.click()
    boton_cancel = driver.find_element(By.XPATH,'//div[@class = "ui-dialog-buttonset"]/button[text()="Cancel Download"]')
    assert boton_cancel.is_displayed() , 'el boton Cancel no se encuentra visible'
    assert boton_cancel.is_enabled() , 'el boton Cancel no se encuentra habilitado'
    driver_wait = WebDriverWait(driver,20)
    boton_close = (By.XPATH,'//div[@class = "ui-dialog-buttonset"]/button[text()="Close"]')
    boton_close = driver_wait.until(ec.visibility_of_element_located(boton_close))
    assert boton_close.is_enabled() , 'el boton Close no se encuentra habilitado'
    boton_close.click()
    driver_wait.until(ec.invisibility_of_element(boton_close))

# def test_progress_bar_implicit():
#     boton_download = driver.find_element(By.ID,'downloadButton')
#     assert boton_download.is_displayed() , 'el boton Download no se encuentra visible'
#     assert boton_download.is_enabled() , 'el boton Download no se encuentra habilitado'
#     boton_download.click()
#     boton_cancel = driver.find_element(By.XPATH,'//div[@class = "ui-dialog-buttonset"]/button[text()="Cancel Download"]')
#     assert boton_cancel.is_displayed() , 'el boton Cancel no se encuentra visible'
#     assert boton_cancel.is_enabled() , 'el boton Cancel no se encuentra habilitado'
#     boton_close = driver.find_element(By.XPATH,'//div[@class = "ui-dialog-buttonset"]/button[text()="Close"]')
#     assert boton_close.is_displayed() , 'No se encuentra el boton Close'
#     assert boton_close.is_enabled() , 'el boton Close no se encuentra habilitado'
#     boton_close.click()
#     boton_close = driver.find_element(By.XPATH,'//div[@class = "ui-dialog-buttonset"]/button[text()="Close"]')
#     assert not boton_close.is_displayed()

def teardown():
    driver.quit()