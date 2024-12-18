
from dotenv import load_dotenv
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

load_dotenv()
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'Users/yadao/Development/chromedriver'


internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider()