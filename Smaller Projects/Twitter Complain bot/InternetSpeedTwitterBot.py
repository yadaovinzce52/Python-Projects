from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        start_test = self.driver.find_element(By.CLASS_NAME, 'start-text')
        start_test.click()

        sleep(60)
        try:
            back_to_results = self.driver.find_element(By.LINK_TEXT, 'Back to test results')
            back_to_results.click()
        except:
            pass
        finally:
            self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        twitter_email = os.getenv('EMAIL')
        twitter_pass = os.getenv('PASSWORD')
        message = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for 1000 down/1000 up?"

        self.driver.get('https://x.com/i/flow/login')
        sleep(5)
        phone = self.driver.find_element(By.NAME, 'text')
        phone.send_keys(twitter_email, Keys.ENTER)
        sleep(1)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(twitter_pass, Keys.ENTER)
        sleep(5)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(message)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()