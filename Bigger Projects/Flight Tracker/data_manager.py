import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/b93fdde380704f0440134416c73b171c/vinzce'sFlightDeals/prices"
        self.headers = {
            "Authorization": f"Bearer {os.environ["AUTHORIZATION"]}",
            "Content-Type": "application/json"
        }
        self.data = []

    def get_data(self):
        response = requests.get(url=self.endpoint, headers=self.headers)

        return [price for price in response.json()['prices']]

    def update_data(self, data, iataCode):
        endpoint = f"https://api.sheety.co/b93fdde380704f0440134416c73b171c/vinzce'sFlightDeals/prices/{data["id"]}"
        body = {
            "price": {
                "iataCode": iataCode,
            }
        }
        response = requests.put(endpoint, headers=self.headers, json=body)
