import requests
import http.client
import json

endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = ''

params = {
    'lat': 0.438255,
    'lon': -84.280731,
    'appid': api_key,
    'cnt': 4
}

response = requests.get(endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = True
for hour_data in weather_data['list']:
    condition = hour_data['weather'][0]['id']
    if int(condition) < 700:
        will_rain = True

conn = http.client.HTTPSConnection("peyrge.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":""}],
            "from": "",
            "text": "Bring an Umbrella!"
        }
    ]
})
headers = {
    'Authorization': '',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))