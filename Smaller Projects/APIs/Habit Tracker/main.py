import requests
import datetime as dt

TOKEN = ''
USERNAME = 'yadaov52'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Take courses',
    'unit': 'hours',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}'

today = dt.datetime.now()

pixel_body = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input('How many hours did you do programming related tasks? ')
}

response = requests.post(pixel_endpoint, json=pixel_body, headers=headers)
print(response.text)

update_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1/20240912'

pixel_update = {
    'quantity': '8',
}

# response = requests.put(update_pixel_endpoint, json=pixel_update, headers=headers)
# print(response.text)

delete_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/graph1/20240912'

# response = requests.delete(delete_pixel, headers=headers)
# print(response.text)