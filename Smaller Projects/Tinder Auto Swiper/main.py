from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL=os.getenv('EMAIL')
PASSWORD=os.getenv('PASSWORD')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.tinder.com/")

sleep(1)
login = driver.find_element(By.XPATH, '//*[@id="q2098069830"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

sleep(1)
facebook = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
facebook.click()

sleep(1)
og_window = driver.window_handles[0]
fb_login = driver.window_handles[1]
driver.switch_to.window(fb_login)

sleep(1)
email_input = driver.find_element(By.NAME, 'email')
password_input = driver.find_element(By.NAME, 'pass')

email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD, Keys.ENTER)

sleep(5)

driver.switch_to.window(og_window)
allow = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow.click()

sleep(1)
miss_out = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
miss_out.click()

sleep(1)
cookies = driver.find_element(By.XPATH, '//*[@id="q2098069830"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()

like = driver.find_element(By.NAME, '//*[@id="q2098069830"]/div/div[1]/div[2]/div/div/main/div/div/div/div/div[4]/div/div[2]/button/span/span[1]')