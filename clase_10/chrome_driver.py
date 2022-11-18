from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = 'drivers/chromedriver.exe'

def create_driver():
    service = Service(DRIVER_PATH)
    return webdriver.Chrome(service=service)
