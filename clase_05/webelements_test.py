from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'
#FIREFOXDRIVER_PATH = 'drivers/geckodriver.exe'
#FIREFOX_PATH = 'C:/Program Files/Mozilla Firefox/firefox.exe' #Verifica instalacion de Firefox (opcional)

URL = 'https://qamindslab.com/'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
# service = Service(FIREFOXDRIVER_PATH)
# options = webdriver.FirefoxOptions()
# options.binary_location = FIREFOX_PATH #opcional
# driver = webdriver.Firefox(service=service,options=options)

driver.get(URL)
driver.maximize_window()
time.sleep(3)

def test_login_laboratorio():
        # Asset
        username = 'David'
        password = 'Password'
        logo = driver.find_element(By.XPATH,'//img[@alt="logo"]')
        assert logo.is_displayed() , 'El logo de QA Minds no esta visible.'
        opcion_laboratorio = driver.find_element(By.XPATH,'//nav[contains(@class,"navbar-menu")]//a[text()="LABORATORIO"]')
        assert opcion_laboratorio.is_displayed() , 'La opcion de LABORATORIO no esta visible'
        opcion_laboratorio.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)

        #Actions
        login_form = driver.find_element(By.CSS_SELECTOR,'.salesforceIdentityLoginForm2')
        assert login_form.is_displayed() , 'El formulario de Login no se encuentra visible'
        input_username = driver.find_element(By.ID,'48:2;a')
        assert input_username.is_displayed() , 'El campo Usuario no esta visible'
        input_username.send_keys(username)
        input_password = driver.find_element(By.XPATH,'//input[@type="password"]')
        assert input_password.is_displayed() , 'El campo Password no esta visible'
        input_password.send_keys(password)
        button_login = driver.find_element(By.TAG_NAME,'button')
        assert button_login.is_displayed() , 'El boton de iniciar sesion no esta visible'
        assert button_login.is_enabled() , 'El button de inicio de sesion no se encuentra habilitado'
        button_login.click()
        time.sleep(3)

        #Assert
        assert not login_form.is_displayed() , 'El formulario de Login sigue visible, cuando no deberia'
        

def teardown():
    driver.quit()