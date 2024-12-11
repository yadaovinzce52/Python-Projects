from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com/home')

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()

login_email = driver.find_element(By.NAME, 'session_key')
login_password = driver.find_element(By.NAME, 'session_password')
login_email.send_keys(EMAIL)
login_password.send_keys(PASSWORD, Keys.ENTER)

driver.get('https://www.linkedin.com/jobs/collections/easy-apply/?currentJobId=4097025328&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII')


jobs_list = driver.find_element(By.CLASS_NAME, 'LDhNwgVkXzAdDalKACWlgkoKiphYwMErfvvp')
jobs_curr_page = jobs_list.find_elements(By.TAG_NAME, 'li')
for job in jobs_curr_page:
    job.click()
    save = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button')
    save.click()

driver.get('https://www.linkedin.com/my-items/saved-jobs/')