from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import factories_drivers.driver_wait as driver_w
from selenium.webdriver.support import expected_conditions as ec
import utils.config_handler as config_handler
import datetime

class BasePage:

    _driver : WebDriver

    def __init__(self,driver) -> None:
        self._driver = driver

    def navigate(self,url):
        self._driver.get(url)

    def close_browser(self):
        self._driver.quit()

    def close_tab(self):
        self._driver.close()

    def _is_present(self,element,mensaje):
        try:
            assert element is not None
        except AssertionError:
            self.take_screenshot(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            raise AssertionError(f'{mensaje}')

    def _get_element(self,by,locator) -> WebElement|None:
        try:
            return self._driver.find_element(by,locator)
        except NoSuchElementException:
            return None

    def _click(self, element:WebElement):
        element.click()

    def _is_enabled(self,element:WebElement,mensaje):
        assert element.is_enabled() , f'{mensaje}'

    def _is_not_enable(self,element:WebElement,mensaje):
        assert not element.is_enabled() , f'{mensaje}'

    def _is_visible(self,element:WebElement, mensaje):
        assert element.is_displayed() , f'{mensaje}'

    def _write(self,element:WebElement,text):
        element.send_keys(text)

    def _get_text(self,element:WebElement) -> str:
        return element.text

    def _is_vanished(self,element,timeout,message):
        w_driver = driver_w.get_driver_wait(self._driver,timeout)
        result = False
        try:
            result = w_driver.until(ec.invisibility_of_element_located(element))
        except TimeoutException as te:
            print(te)
        assert result , f'{message}'

    def _is_clickable(self,element,timeout,message):
        w_driver = driver_w.get_driver_wait(self._driver,timeout)
        result = False
        try:
            result = w_driver.until(ec.element_to_be_clickable(element))
        except TimeoutException as te:
            print(te)
        assert result , f'{message}'
    
    def take_screenshot(self,filename=datetime.datetime.now().strftime("%Y%m%d%H%M%S")):
        self._driver.save_screenshot(f'{config_handler.get_path_screenshots()}/{filename}.png')
    