from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'
URL = 'https://laboratorio.qaminds.com/'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)
driver.get(URL)
driver.maximize_window()


def test_busqueda_producto():
    
    # Asset
    product_name = 'iPhone'
    search_title_expected = 'Search - iPhone'
    search_criterial_expected = 'Products meeting the search criteria'

    img_logo = driver.find_element(By.XPATH,'//div[@id="logo"]//img')
    assert img_logo.is_displayed() , 'No se encuentra el logo en la pagina de inicio'

    # Actions
    input_search = driver.find_element(By.NAME,'search')
    assert input_search.is_displayed() , 'No se encuentra el input Search'
    input_search.send_keys(product_name)
    button_search = driver.find_element(By.XPATH,'//div[@id="search"]//button')
    assert button_search.is_displayed() , 'No se encuentra el boton de Search'
    assert button_search.is_enabled() , 'El boton de Search se encuentra inhabilitado'
    button_search.click()

    #Asserts
    title_search = driver.find_element(By.TAG_NAME,'h1')
    assert title_search.is_displayed() , 'El titulo de la busqueda no fue encontrado'
    assert search_title_expected == title_search.text , 'El texto del Titulo de la Busqueda no coincide con el esperado'
    criterial_search = driver.find_element(By.TAG_NAME,'h2')
    assert criterial_search.is_displayed() , 'El titulo de Criterio de Busqueda no fue encontrado'
    assert search_criterial_expected == criterial_search.text , 'El texto del Criterio de Busqueda no coincide con el esperado'
    img_product = driver.find_element(By.XPATH,'//img[@title="iPhone"]')
    assert img_product.is_displayed() , 'La imagen esperada no se encuenrtra visible'
    product_title = driver.find_element(By.XPATH,'//div[@class="caption"]//a')
    assert product_title.is_displayed(), 'No se encuentra el titulo del producto'
    assert product_name == product_title.text , 'No coincide el nombre del producto esperado'


def teardown():
    driver.quit()