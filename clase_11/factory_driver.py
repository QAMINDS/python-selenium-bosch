from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, WebDriverException
import chrome_driver
import firefox_driver
import edge_driver
import config_handler

driver : WebDriver

def get_driver():
    global driver
    config_handler.load_config()
    browser_name = config_handler.get_browser_name()
    if browser_name == 'chrome':
        driver = chrome_driver.create_driver()
    elif browser_name == 'firefox':
        driver = firefox_driver.create_driver()
    elif browser_name == 'edge':
        driver = edge_driver.create_driver()
    else:
        raise NameError(f'No existe driver para el navegador: {browser_name}')

    __set_headless()
    __set_maximized()
    __set_implicitly_wait()
    __set_page_load()
    __navigate_to_start()

    return driver

def __set_headless():
    if config_handler.get_headless():
        driver.set_window_size(config_handler.get_width(),config_handler.get_height())

def __set_maximized():
    if config_handler.get_maximized():
        driver.maximize_window()

def __set_implicitly_wait():
    driver.implicitly_wait(config_handler.get_implicit_wait())

def __set_page_load():
    driver.set_page_load_timeout(config_handler.get_page_load())

def __navigate_to_start():
    url = config_handler.get_url()
    try:
        driver.get(url)
    except TimeoutException:
        driver.quit()
        assert False , f'No se pudo cargar la pagina {url} en {config_handler.get_page_load()} segundos'
    except WebDriverException:
        driver.quit()
        assert False , f'La pagina {url} no esta diponible'