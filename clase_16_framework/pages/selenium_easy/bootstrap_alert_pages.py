from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BootstrapAlertPage(BasePage):

    __title_text = {'by':By.CSS_SELECTOR,'locator':'h8'}
    __button_autocloseable = {'by':By.ID,'locator':'autoclosable-btn-success'}
    __message_alert = {'by':By.XPATH,'locator':'//div[contains(@class,"autocloseable-success")]'}

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.__verify_page()

    def __verify_page(self):
        title_element = self._get_element(self.__title_text['by'],self.__title_text['locator'])
        self._is_present(title_element, 'No se encuentra el titulo Bootstrap Alert Message')
        self._is_visible(title_element, 'El Titulo de Bootstrap Alert Message no esta Visible')

    def click_on_autoclose_success(self):
        button_autocloseable = self._get_element(self.__button_autocloseable['by'],self.__button_autocloseable['locator'])
        self._is_present(button_autocloseable,'No se encuentra el Boton de Autocloseable Success Message')
        self._is_visible(button_autocloseable,'El Boton de Autocloseable Success Message no esta Visible')
        self._is_enabled(button_autocloseable,'El Boton de Autocloseable Success Message no esta Habilitado')
        self._click(button_autocloseable)

    def verify_autocloseable_not_enable(self):
        button_autocloseable = self._get_element(self.__button_autocloseable['by'],self.__button_autocloseable['locator'])
        self._is_present(button_autocloseable,'No se encuentra el Boton de Autocloseable Success Message')
        self._is_not_enable(button_autocloseable,'El Boton de Autocloseable Success Message se encuentra Habilitado')

    def verify_message_alert_visible(self):
        message_element = self._get_element(self.__message_alert['by'],self.__message_alert['locator'])
        self._is_present(message_element,'No se encuentra el Mensaje de Autocloseable Success Message')
        self._is_visible(message_element,'El mensaje de Autocloseable Success Message no esta Visible')

    def verify_message_alert_invisible(self,timeout):
        message_element = self._get_element(self.__message_alert['by'],self.__message_alert['locator'])
        self._is_present(message_element,'No se encuentra el Mensaje de Autocloseable Success Message')
        self._is_vanished(message_element,timeout,'El Mensaje de Alerta se encuentra aun visibible')

    def verify_autocloseable_clickable(self,timeout):
        button_autocloseable = self._get_element(self.__button_autocloseable['by'],self.__button_autocloseable['locator'])
        self._is_present(button_autocloseable,'No se encuentra el Boton de Autocloseable Success Message')
        self._is_clickable(button_autocloseable,timeout,'El Boton de Autocloseable aun no es clickable')