from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

CHROMEDRIVER_PATH = 'clase_01/drivers/chromedriver.exe'
FIREFOXDRIVER_PATH = 'clase_01/drivers/geckodriver.exe'

URL = 'https://qamindslab.com/'


service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)


driver.get(URL)
time.sleep(3)
driver.close()