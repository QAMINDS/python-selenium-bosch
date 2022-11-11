from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'
URL = 'https://laboratorio.qaminds.com/'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)


def setup():
    driver.get(URL)
    driver.maximize_window()
    time.sleep(3)
    img_logo = driver.find_element(By.CSS_SELECTOR,'#logo img')
    assert img_logo.is_displayed() , 'No se encuentra el logo de la pagina'
    slideshow = driver.find_element(By.ID,'slideshow0')
    assert slideshow.is_displayed(), 'No se encuentra el Slideshow en la pagina' 


def test_busqueda_by_menu_tablet():
    option_tablet = driver.find_element(By.XPATH,'//nav[@id="menu"]//a[text()="Tablets"]')
    assert option_tablet.is_displayed() ,'No se encuentra el menu Tablet'
    assert option_tablet.is_enabled() , 'El menu Tablet se encuentra Deshabilitado'
    option_tablet.click()
    # Verificar elemento content
    # Verificar Titulo
    # Verificar carga de Tablet Samsung (Imagen y Titulo del producto)
    # Hacer click a Imagen o Titulo para seleccionar
    # Verificar Precio
    # Verificar Wishlist
    # Verificar Add Cart


def teardown():
    driver.quit()