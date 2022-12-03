from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MenuPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    __boton_buscar = '#search button'

    def click_boton_buscar(self):
        button_element = self._get_element(By.CSS_SELECTOR, self.__boton_buscar)
        self._is_present(button_element, 'No se encuentra el boton Buscar')
        self._is_visible(button_element, 'El boton buscar no se encuentra visible') 
        self._is_enabled(button_element, 'El boton de Busqueda no se encuentra habilitado') 
        self._click(button_element)
        