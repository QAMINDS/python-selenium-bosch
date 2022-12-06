from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MenuPage(BasePage):

    __button_search = {'by':By.CSS_SELECTOR, 'locator':'#search button'}
    __input_buscar = {'by':By.NAME,'locator':'search'}
    __img_logo = {'by':By.CSS_SELECTOR,'locator':'#logo img'}

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verificar_menu()
        
    def __verificar_menu(self):
        img_element = self._get_element(self.__img_logo['by'],self.__img_logo['locator'])
        self._is_present(img_element,'No se encuentra la Imagen del Logo')
        self._is_visible(img_element,'El Logo no se encuentra visible')

    def click_boton_buscar(self):
        button_element = self._get_element(self.__button_search['by'], self.__button_search['locator'])
        self._is_present(button_element, 'No se encuentra el boton Buscar')
        self._is_visible(button_element, 'El boton buscar no se encuentra visible') 
        self._is_enabled(button_element, 'El boton de Busqueda no se encuentra habilitado') 
        self._click(button_element)

    def ingresar_busqueda(self,text):
        input_element = self._get_element(self.__input_buscar['by'],self.__input_buscar['locator'])
        self._is_present(input_element,'No se encuentra el input de Busqueda')
        self._is_visible(input_element,'El input de Busqueda no se encuentra visible')
        self._write(input_element,text)

    def buscar_producto(self,text):
        self.ingresar_busqueda(text)
        self.click_boton_buscar()