from selenium.webdriver.support.wait import WebDriverWait

def get_driver_wait(driver, timeout):
    return WebDriverWait(driver,timeout)