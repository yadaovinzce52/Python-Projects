import os
from dotenv import load_dotenv
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

load_dotenv()
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'Users/yadao/Development/chromedriver'
TWITTER_EMAIL = os.getenv('EMAIL')
TWITTER_PASSWORD = os.getenv('PASSWORD')

internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider()