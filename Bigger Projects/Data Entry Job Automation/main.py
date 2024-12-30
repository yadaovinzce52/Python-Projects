import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_page = response.text

soup = BeautifulSoup(zillow_page, 'html.parser')
all_listings = soup.find_all('li', attrs={'class': 'ListItem-c11n-8-84-3-StyledListCardWrapper'})
listing_links = [listing.find('a').get('href') for listing in all_listings]
listing_prices = [listing.find('span').text[:-4] for listing in all_listings]
listing_addresses = [listing.find('address').text.strip() for listing in all_listings]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(all_listings)):
    driver.get(
        'https://docs.google.com/forms/d/e/1FAIpQLSfQiyF0QWNYT99cCT7J4rQgAjwrtnIuobQI7QBtCkMzeSh_0g/viewform?usp=header')

    time.sleep(1)

    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address_input.send_keys(listing_addresses[i])
    price_input.send_keys(listing_prices[i])
    link_input.send_keys(listing_links[i])
    submit.click()


