import factories_drivers.factory_driver as f_driver
from pages.menu_page import MenuPage
from pages.base_page import BasePage
from pages.search_page import SearchPage
import time

driver = f_driver.get_driver()

def test_boton_buscar():
    producto = 'Display'
    busqueda_invalida_text = 'There is no product that matches the search criteria.'
    menu_page = MenuPage(driver) 
    menu_page.buscar_producto(producto)
    search_page = SearchPage(driver)
    search_page.verificar_no_producto(busqueda_invalida_text)
    search_page.check_product_description()
    search_page.click_search()
    time.sleep(2)

def teardown():
    BasePage(driver).close_browser()