import chrome_driver
import firefox_driver
import edge_driver

#URL = 'https://laboratorio.qaminds.com/'
URL = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'

def get_driver(browser_name):
    if browser_name == 'chrome':
        driver = chrome_driver.create_driver()
    elif browser_name == 'firefox':
        driver = firefox_driver.create_driver()
    elif browser_name == 'edge':
        driver = edge_driver.create_driver()
    else:
        raise NameError(f'No existe driver para el navegador: {browser_name}')

    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get(URL)
    return driver