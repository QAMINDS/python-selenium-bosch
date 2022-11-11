from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'
URL = 'https://demoqa.com/select-menu'

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get(URL)
driver.maximize_window()
time.sleep(3)

# def test_old_select():
#     # Asset
#     title_expected = 'Select Menu'
#     option = 'Purple'
#     option_value = '4'
#     title = driver.find_element(By.CLASS_NAME,'main-header')
#     assert title.is_displayed() , 'No se encuentra el titulo de la pagina'
#     assert title_expected == title.text , 'No coresponde la opcion del titulo'

#     #Actions
#     menu = driver.find_element(By.ID,'oldSelectMenu')
#     assert menu.is_displayed() , 'No se encuentra el Combo de Menu'
#     assert menu.is_enabled(), 'No se puede interactuar con el Combo de Menu'
#     menu_list = Select(menu)
#     menu_list.select_by_index(option_value)
#     option_selected = menu_list.first_selected_option
#     #Assert
#     assert option == option_selected.text , 'No se selecciono la opcion deseada'
#     time.sleep(3)

def test_new_select():
    # Asset
    title_expected = 'Select Menu'
    option_expected = 'Mrs.'
    title = driver.find_element(By.CLASS_NAME,'main-header')
    assert title.is_displayed() , 'No se encuentra el titulo de la pagina'
    assert title_expected == title.text , 'No coresponde la opcion del titulo'

    #Actions
    menu = driver.find_element(By.ID,'selectOne')
    assert menu.is_displayed() , 'No se encuentra el Combo de Menu'
    assert menu.is_enabled(), 'No se puede interactuar con el Combo de Menu'
    menu.click() #abrir Menu
    option_list = driver.find_element(By.XPATH,f'//*[contains(text(),"{option_expected}")]')
    assert option_list.is_displayed() , 'No se encuentra la opcion a seleccionar'
    option_list.click()

    #Assert
    option_selected = driver.find_element(By.XPATH,'//div[contains(@class,"singleValue")]')
    assert option_selected.is_displayed() , 'Ne se encuentra la opcion seleccionada visible'
    assert option_expected == option_selected.text , 'No se selecciono la opcion deseada'
    time.sleep(2)
    

def teardown():
    driver.quit()