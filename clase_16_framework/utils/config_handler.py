import json

PATH_FILE = './config.json'

__config = None

def load_config():
    global __config
    with open(PATH_FILE,'r') as file:
        __config = json.load(file)

def get_browser_name():
    return __config['browser_name']

def get_url():
    return __config['url']

def get_incognito():
    return __config['incognito']

def get_headless():
    return __config['headless']['enabled']

def get_width():
    return __config['headless']['resolution']['x']

def get_height():
    return __config['headless']['resolution']['y']

def get_maximized():
    return __config['maximized_window']

def get_implicit_wait():
    return __config['implicit_wait']

def get_page_load():
    return __config['page_load']