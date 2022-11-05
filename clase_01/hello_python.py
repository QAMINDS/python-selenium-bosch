from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

#CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'
FIREFOXDRIVER_PATH = 'drivers/geckodriver.exe'
FIREFOX_PATH = 'C:/Program Files/Mozilla Firefox/firefox.exe' #Verifica instalacion de Firefox (opcional)

URL = 'https://qamindslab.com/'


#service = Service(CHROMEDRIVER_PATH)
#driver = webdriver.Chrome(service=service)
service = Service(FIREFOXDRIVER_PATH)
options = webdriver.FirefoxOptions()
options.binary_location = FIREFOX_PATH #opcional
driver = webdriver.Firefox(service=service,options=options)


driver.get(URL)
elemento = driver.find_element(By.ID,'ID')
elemento.click()
time.sleep(3)
driver.close()