import factory_driver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    #Before Each TestCase
    global driver
    driver = factory_driver.get_driver()
    # TestCase
    yield driver
    #After Each Testcase
    driver.quit()

def test_get(setup):
    url = 'https://qamindslab.com/'
    expected_title = 'QA Minds Lab'
    driver.get(url)
    assert expected_title == driver.title , 'No coincide el Titulo de la pagina'
    assert url == driver.current_url , 'La URL de la pagina no coincinde con el esperado'


def test_product(setup):
    #asset
    url = 'https://laboratorio.qaminds.com/index.php?route=product/product&product_id=40&search=iphone'
    driver.get(url)

    #Actions
    button_add_cart = driver.find_element(By.ID,'button-cart')

    #Assert
    assert button_add_cart.is_displayed() , 'No se encuentra el boton Agregar al Carro'
