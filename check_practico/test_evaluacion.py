import factory_driver
from selenium.webdriver.common.by import By
import time

driver = factory_driver.get_driver()

def test_busqueda_display():
    url_expected = 'https://laboratorio.qaminds.com/'
    search_text = 'Display'
    expected_search_criteria = 'There is no product that matches the search criteria.'
    apple_cinema = 'Apple Cinema 30"'
    ipod_nano = 'iPod Nano'
    ipod_touch = 'iPod Touch'
    macbook_pro = 'MacBook Pro'
    assert url_expected == driver.current_url , 'La URL no es la esparada'
    img_logo = driver.find_element(By.XPATH,'//div[@id="logo"]//img')
    assert img_logo.is_displayed() , 'La imagen del Logo no esta visible'
    input_search = driver.find_element(By.NAME,'search')
    assert input_search.is_displayed() , 'El input de Busqueda no se encuentra visible'
    assert input_search.is_enabled() , 'El input de Busqueda no se encuentra habilitado para escribir'
    input_search.send_keys(search_text)
    button_search = driver.find_element(By.CSS_SELECTOR,'#search button')
    assert button_search.is_displayed() , 'El Boton de Busqueda no se encuentra visible'
    assert button_search.is_enabled() , 'El Boton de Busqueda no se encuentra habilitado'
    button_search.click()
    text_search = driver.find_element(By.XPATH,'//p[contains(text(),"no product")]')
    assert text_search.is_displayed() , 'No se mostro el mensaje de no se encontro el Producto'
    assert expected_search_criteria == text_search.text , 'No coincide el mensaje experado con el obtenido para el criterio de Busqueda'
    checkbox_search = driver.find_element(By.ID,'description')
    assert checkbox_search.is_displayed() , 'El checkbox de Search Product no se encuentra visible'
    assert checkbox_search.is_enabled() , 'El checkbox de Search no se encuentra habilitado'
    assert not checkbox_search.is_selected() , 'El checkbox se encuentra seleccionado'
    checkbox_search.click()
    button_search_description = driver.find_element(By.ID,'button-search')
    assert button_search_description.is_displayed() , 'El boton de Search Description no se encuentra visible'
    assert button_search_description.is_enabled() , 'El boton de Search Description no se encuentra habilitado'
    button_search_description.click()
    text_title_product = get_product_title(apple_cinema)
    assert text_title_product.is_displayed() , 'No se encuentra el titulo de Apple Cinema'
    assert apple_cinema == text_title_product.text , 'El Titulo del producto de Apple Cinema no coincide'
    text_title_product = get_product_title(ipod_nano)
    assert text_title_product.is_displayed() , 'No se encuentra el titulo de iPod Nano'
    assert ipod_nano == text_title_product.text , 'El Titulo del producto de iPod Nano no coincide'
    text_title_product = get_product_title(ipod_touch)
    assert text_title_product.is_displayed() , 'No se encuentra el titulo de iPod Touch'
    assert ipod_touch == text_title_product.text , 'El Titulo del producto de iPod Touch no coincide'
    text_title_product = get_product_title(macbook_pro)
    assert text_title_product.is_displayed() , 'No se encuentra el titulo de MacBook Pro'
    assert macbook_pro == text_title_product.text , 'El Titulo del producto de MacBook Pro no coincide'
    

def teardown():
    driver.quit()

def get_product_title(product_name):
    return driver.find_element(By.XPATH,f"//div[@class='caption']//a[text()='{product_name}']")