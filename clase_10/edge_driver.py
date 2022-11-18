from selenium import webdriver
from selenium.webdriver.edge.service import Service

DRIVER_PATH = 'drivers/msedgedriver.exe'

def create_driver():
    service = Service(DRIVER_PATH)
    return webdriver.Edge(service=service)
