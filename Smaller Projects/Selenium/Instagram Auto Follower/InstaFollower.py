import os
import random

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

load_dotenv()

class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        username = os.getenv('IG_USERNAME')
        password = os.getenv('IG_PASSWORD')
        self.driver.get('https://www.instagram.com/')
        self.driver.implicitly_wait(1)
        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        username_input.send_keys(username)
        password_input.send_keys(password, Keys.ENTER)
        self.driver.implicitly_wait(5)
        save_login = self.driver.find_element(By.XPATH, '//div[contains(text(), "Not now")]')
        save_login.click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/smitegame/')

        # Used their followings because it is significantly less people
        following = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]')
        following.click()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                self.driver.implicitly_wait(random.randint(1, 5))
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

