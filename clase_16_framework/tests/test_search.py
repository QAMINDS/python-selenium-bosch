import factories_drivers.factory_driver as f_driver
from pages.menu_page import MenuPage
from pages.base_page import BasePage

driver = f_driver.get_driver()

def test_boton_buscar():
    menu_page = MenuPage(driver)
    menu_page.click_boton_buscar()

def teardown():
    BasePage(driver).close_browser()