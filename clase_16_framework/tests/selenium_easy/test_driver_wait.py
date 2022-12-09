import factories_drivers.factory_driver as f_driver
from pages.base_page import BasePage
from pages.selenium_easy.bootstrap_alert_pages import BootstrapAlertPage
import time

class TestSeleniumEasy:

    URL = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'

    def setup_method(self):
        self._driver = f_driver.get_driver()
        BasePage(self._driver).navigate(self.URL)

    def test_alert_message_boton_3s(self):
        bootstrap_page = BootstrapAlertPage(self._driver)
        bootstrap_page.click_on_autoclose_success()
        bootstrap_page.verify_autocloseable_not_enable()
        bootstrap_page.verify_message_alert_visible()
        bootstrap_page.verify_message_alert_invisible(3)
        bootstrap_page.verify_autocloseable_clickable(3)
        bootstrap_page.take_screenshot()

    def test_alert_message_boton_30s(self):
        bootstrap_page = BootstrapAlertPage(self._driver)
        bootstrap_page.click_on_autoclose_success()
        bootstrap_page.verify_autocloseable_not_enable()
        bootstrap_page.verify_message_alert_visible()
        bootstrap_page.verify_message_alert_invisible(30)
        bootstrap_page.verify_autocloseable_clickable(30)
        bootstrap_page.take_screenshot()

    def teardown_method(self):
        BasePage(self._driver).close_browser()