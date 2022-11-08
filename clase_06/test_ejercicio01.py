from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'
URL = 'https://laboratorio.qaminds.com/'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(URL)
driver.maximize_window()
time.sleep(3)

def test_busqueda_producto():
    
    # Asset
    product_name = 'iphone'
    search_title_expected = 'Search - iphone'
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
    time.sleep(5)
    title_search = driver.find_element(By.TAG_NAME,'h1')
    assert title_search.is_displayed() , 'El titulo de la busqueda no fue encontrado'
    assert search_title_expected == title_search.text , 'El texto del Titulo de la Busqueda no coincide con el esperado'
    criterial_search = driver.find_element(By.TAG_NAME,'h2')
    assert criterial_search.is_displayed() , 'El titulo de Criterio de Busqueda no fue encontrado'
    assert search_criterial_expected == criterial_search.text , 'El texto del Criterio de Busqueda no coincide con el esperado'
    img_product = driver.find_element(By.XPATH,'//img[@title="iPhone"]')
    assert img_product.is_displayed() , 'La imagen esperada no se encuenrtra visible'

def test_busqueda_no_producto():
    
    # Asset
    product_name = 'nokia'
    search_title_expected = 'Search - nokia'
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
    time.sleep(5)
    title_search = driver.find_element(By.TAG_NAME,'h1')
    assert title_search.is_displayed() , 'El titulo de la busqueda no fue encontrado'
    assert search_title_expected == title_search.text , 'El texto del Titulo de la Busqueda no coincide con el esperado'
    criterial_search = driver.find_element(By.TAG_NAME,'h2')
    assert criterial_search.is_displayed() , 'El titulo de Criterio de Busqueda no fue encontrado'
    assert search_criterial_expected == criterial_search.text , 'El texto del Criterio de Busqueda no coincide con el esperado'
    text_result = driver.find_element(By.XPATH,'//div[@id="content"]/p[contains(text(),"no product")]')
    assert text_result.is_displayed() , 'El mensaje de resultado no se encuenrtra visible'

def teardown():
    driver.quit()