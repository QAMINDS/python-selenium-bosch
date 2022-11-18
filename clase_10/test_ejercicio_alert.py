from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import factory_driver
import driver_wait

driver = factory_driver.get_driver('firefox')

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
    wait_driver = driver_wait.get_driver_wait(driver,timeout)
    try:
        wait_driver.until(ec.element_to_be_clickable(element))    
        return True
    except TimeoutException as te:
        return False

def verify_element_invisible(element,timeout):
    wait_driver = driver_wait.get_driver_wait(driver,timeout)
    try:
        wait_driver.until(ec.invisibility_of_element_located(element))    
        return True
    except TimeoutException as te:
        return False

def teardown():
    driver.quit()
