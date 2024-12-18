import requests
import http.client
import json


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_endpoint = 'https://www.alphavantage.co/query'
stock_api_key = ''

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': stock_api_key,
}

response = requests.get(stock_endpoint, params=stock_params)
response.raise_for_status()
stock_data = response.json()

day_before_yesterday = float(stock_data['Time Series (Daily)']['2024-09-06']['4. close'])
yesterday = float(stock_data['Time Series (Daily)']['2024-09-09']['4. close'])

diff_percent = int((yesterday - day_before_yesterday) / yesterday * 100)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_endpoint = 'https://newsapi.org/v2/everything'
news_api_key = ''

news_params = {
    'q': COMPANY_NAME,
    'apikey': news_api_key,
    'pageSize': 3
}

if diff_percent >= 5 or diff_percent <= -5:
    news_response = requests.get(news_endpoint, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    news_pieces = news_data['articles']
    print(news_pieces)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    for piece in news_pieces:
        conn = http.client.HTTPSConnection("peyrge.api.infobip.com")
        payload = json.dumps({
            "messages": [
                {
                    "destinations": [{"to": ""}],
                    "from": "",
                    "text": f"TSLA: 🔺{diff_percent}%\n"
                            f"Headline: {piece['title']}\n"
                            f"Brief: {piece['content']}"
                }
            ]
        })
        headers = {
            'Authorization': 'App ',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        conn.request("POST", "/sms/2/text/advanced", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

