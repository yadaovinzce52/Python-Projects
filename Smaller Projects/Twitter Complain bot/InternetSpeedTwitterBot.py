from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


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
            print(self.down)
            print(self.up)

    def tweet_at_provider(self):
        pass

