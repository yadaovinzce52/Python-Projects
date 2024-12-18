from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time

def start_click():
    end_time = time.time() + 1
    while time.time() < end_time:
        cookie = driver.find_element(By.ID, 'cookie')
        cookie.click()

    return

def start_game():
    end_time = time.time() + 20
    while time.time() < end_time:
        start_click()

        store = driver.find_element(By.ID, 'store')
        store_items = store.find_elements(By.TAG_NAME, 'div')

        for store_item in store_items[::-1]:
            color = store_item.value_of_css_property('background-color')
            color_hex = Color.from_string(color).hex
            if color_hex.upper() == '#EEEEEE':
                store_item.click()
                break

        start_click()

    return

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

start_game()
cookies_per_second = driver.find_element(By.ID, 'cps')
print(cookies_per_second.text)