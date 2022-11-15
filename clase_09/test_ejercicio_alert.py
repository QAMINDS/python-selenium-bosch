from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'
URL = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get(URL)

#Modo 1 - Espero por invisibilidad de mensaje
# def test_alert_message():
#     #Assets
#     title_alert = driver.find_element(By.CSS_SELECTOR,'h2')
#     assert title_alert.is_displayed() , 'No se encuentra el titulo Bootstrap Alert Message'
#     driver_wait = WebDriverWait(driver,6)

#     #Actions
#     button_autocloseable = driver.find_element(By.ID,'autoclosable-btn-success')
#     assert button_autocloseable.is_displayed() , 'No se encuentra el boton de Autocloseable'
#     assert button_autocloseable.is_enabled() , 'El boton de Autocloseable no se encuentra habilitado'
#     button_autocloseable.click()
#     assert not button_autocloseable.is_enabled() , 'El boton de Autocloseable se encuentra habilitado'
#     message_alert = driver.find_element(By.XPATH,'//div[contains(@class,"autocloseable-success")]')
#     assert message_alert.is_displayed() , 'No se encuentra visible el mensaje de alerta'
    
#     #Asserts
#     driver_wait.until(ec.invisibility_of_element_located(message_alert))
#     assert button_autocloseable.is_enabled() , 'El boton de Autocloseable no se encuentra habilitado'

#Modo 2 - Espero por Habilitacion de boton
def test_alert_message_boton():
    #Assets
    title_alert = driver.find_element(By.CSS_SELECTOR,'h2')
    assert title_alert.is_displayed() , 'No se encuentra el titulo Bootstrap Alert Message'
    driver_wait = WebDriverWait(driver,6)

    #Actions
    button_autocloseable = driver.find_element(By.ID,'autoclosable-btn-success')
    assert button_autocloseable.is_displayed() , 'No se encuentra el boton de Autocloseable'
    assert button_autocloseable.is_enabled() , 'El boton de Autocloseable no se encuentra habilitado'
    button_autocloseable.click()
    assert not button_autocloseable.is_enabled() , 'El boton de Autocloseable se encuentra habilitado'
    message_alert = driver.find_element(By.XPATH,'//div[contains(@class,"autocloseable-success")]')
    assert message_alert.is_displayed() , 'No se encuentra visible el mensaje de alerta'
    
    #Asserts
    driver_wait.until(ec.element_to_be_clickable(button_autocloseable))
    assert not message_alert.is_displayed() , 'El boton de Autocloseable no se encuentra habilitado'

#Modo 3 - Full Espera Explicita
def test_alert_message_boton():
    #Assets
    title_alert = driver.find_element(By.CSS_SELECTOR,'h2')
    assert title_alert.is_displayed() , 'No se encuentra el titulo Bootstrap Alert Message'

    #Actions
    button_autocloseable = driver.find_element(By.ID,'autoclosable-btn-success')
    assert button_autocloseable.is_displayed() , 'No se encuentra el boton de Autocloseable'
    assert button_autocloseable.is_enabled() , 'El boton de Autocloseable no se encuentra habilitado'
    button_autocloseable.click()
    assert not button_autocloseable.is_enabled() , 'El boton de Autocloseable se encuentra habilitado'
    message_alert = driver.find_element(By.XPATH,'//div[contains(@class,"autocloseable-success")]')
    assert message_alert.is_displayed() , 'No se encuentra visible el mensaje de alerta'
    
    #Asserts
    assert verify_element_invisible(message_alert,7) , 'El Mensaje de Alerta se encuentra aun visbible'
    assert verify_element_clickable(button_autocloseable,6) , 'El Boton de Autocloseable aun no es clickable'
    

def verify_element_clickable(element,timeout):
    driver_wait = WebDriverWait(driver,timeout)
    try:
        driver_wait.until(ec.element_to_be_clickable(element))    
        return True
    except TimeoutException as te:
        return False

def verify_element_invisible(element,timeout):
    driver_wait = WebDriverWait(driver,timeout)
    try:
        driver_wait.until(ec.invisibility_of_element_located(element))    
        return True
    except TimeoutException as te:
        return False

def teardown():
    driver.quit()
