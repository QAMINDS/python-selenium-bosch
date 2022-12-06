from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    __content_search = {'by':By.ID,'locator':'content'}
    __text_no_product = {'by':By.XPATH,'locator':'//div[@id="content"]//p[2]'}
    __check_desciption = {'by':By.ID,'locator':'description'}
    __button_search = {'by':By.ID,'locator':'button-search'}

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verificar_pagina_busqueda()

    def __verificar_pagina_busqueda(self):
        content_element = self._get_element(self.__content_search['by'],self.__content_search['locator'])
        self._is_present(content_element,'No se encuentra el contenedor de la Busqueda')
        self._is_visible(content_element,'El Contenedor de la Busqueda no se encuentra visible')

    def verificar_no_producto(self,text_expected):
        text_no_product_element = self._get_element(self.__text_no_product['by'],self.__text_no_product['locator'])
        self._is_present(text_no_product_element,'No se encuentra el texto de Producto no encontrado')
        self._is_visible(text_no_product_element,'El texto del Producto no encontrado no se encuentra visible')
        actual_text = self._get_text(text_no_product_element)
        assert text_expected == actual_text , f'El mensaje de Producto no encontrado, no coincide. Se esperaba "{text_expected}" y se obtuvo "{actual_text}"'

    def check_product_description(self):
        check_element = self._get_element(self.__check_desciption['by'],self.__check_desciption['locator'])
        self._is_present(check_element,'No se encuentra el Check de Producto')
        self._is_visible(check_element,'El Check de Producto no se encuentra Visible')
        self._is_enabled(check_element,'El Check de Producto no se encuentra Habilitado')
        self._click(check_element)

    def click_search(self):
        button_element = self._get_element(self.__button_search['by'],self.__button_search['locator'])
        self._is_present(button_element,'No se encuentra el Boton de Search')
        self._is_visible(button_element,'El Boton de Search no se encuentra Visible')
        self._is_enabled(button_element,'El Boton de search no se encuentra Habilitado')
        self._click(button_element)