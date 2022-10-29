from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pytest

CHROMEDRIVER_PATH = 'clase_01/drivers/chromedriver.exe'


driver = None

def setup():
    global driver
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

@pytest.mark.qaminds
def test_qamindlab():
    url = 'https://qamindslab.com/'
    driver.get(url)

def test_youtube():
    url = 'https://youtube.com/'
    driver.get(url)

@pytest.mark.google
def test_google():
    url = 'https://google.com/'
    driver.get(url)
    

def teardown():
    time.sleep(3)
    driver.close()