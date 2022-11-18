import factory_driver
from selenium.webdriver.common.by import By


def setup():
    global driver
    driver = factory_driver.get_driver('edge')

def test_get():
    url = 'https://qamindslab.com/'
    expected_title = 'QA Minds Lab'
    driver.get(url)
    assert expected_title == driver.title , 'No coincide el Titulo de la pagina'
    assert url == driver.current_url , 'La URL de la pagina no coincinde con el esperado'

def test_back():
    url = 'https://qamindslab.com/'
    new_url = 'http://laboratorio.qaminds.com/'
    expected_title = 'QA Minds Lab'
    driver.get(url)
    driver.get(new_url)
    driver.back()
    assert expected_title == driver.title , 'No coincide el Titulo de la pagina'
    assert url == driver.current_url , 'La URL de la pagina no coincinde con el esperado'

def test_forward():
    url = 'https://qamindslab.com/'
    new_url = 'http://laboratorio.qaminds.com/'
    expected_title = 'Your Store'
    driver.get(url)
    driver.get(new_url)
    driver.back()
    driver.forward()
    assert expected_title == driver.title , 'No coincide el Titulo de la pagina'
    assert new_url == driver.current_url , 'La URL de la pagina no coincinde con el esperado'

def test_product():
    #asset
    url = 'https://laboratorio.qaminds.com/index.php?route=product/product&product_id=40&search=iphone'
    driver.get(url)

    #Actions
    button_add_cart = driver.find_element(By.ID,'button-cart')

    #Assert
    assert button_add_cart.is_displayed() , 'No se encuentra el boton Agregar al Carro'

def teardown():
    driver.quit()