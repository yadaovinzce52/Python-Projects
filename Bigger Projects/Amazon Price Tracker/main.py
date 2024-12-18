from pprint import pprint

from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-APIs": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

pprint(soup)

price = soup.find("span", attrs={"class": "aok-offscreen"}).get_text()
product = soup.find(id="productTitle").get_text().strip()

price_num = float(price.split("$")[1])

email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

BUY_PRICE = 100

if price_num < BUY_PRICE:
    with smtplib.SMTP(os.getenv("SMTP_ADDRESS")) as gmail:
        gmail.starttls()
        gmail.login(user=email, password=password)
        gmail.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject: Amazon Price Alert!\n\n{product} is now ${price_num}\n{url}".encode("utf-8")
        )