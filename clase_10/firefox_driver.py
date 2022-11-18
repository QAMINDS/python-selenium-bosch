from selenium import webdriver
from selenium.webdriver.firefox.service import Service


DRIVER_PATH = 'drivers/geckodriver.exe'
FIREFOX_PATH = 'C:/Program Files/Mozilla Firefox/firefox.exe'

def create_driver():
    service = Service(DRIVER_PATH)
    options = webdriver.FirefoxOptions()
    options.binary_location = FIREFOX_PATH
    return webdriver.Firefox(service=service,options=options)