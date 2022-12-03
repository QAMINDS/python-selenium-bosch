from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

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
        assert element is not None , f'{mensaje}'


    def _get_element(self,by,locator) -> WebElement|None:
        try:
            return self._driver.find_element(by,locator)
        except NoSuchElementException:
            return None

    def _click(self, element:WebElement):
        element.click()

    def _is_enabled(self,element:WebElement,mensaje):
        assert element.is_enabled() , f'{mensaje}'

    def _is_visible(self,element:WebElement, mensaje):
        assert element.is_displayed() , f'{mensaje}'
