import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.access_token = self.get_token()


    def get_flights(self, city):
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(endpoint, params=params, headers=header)
        try:
            return response.json()["data"][0]["iataCode"]
        except IndexError:
            return "N/A"
        except KeyError:
            return "Not Found"

    @staticmethod
    def get_token():
        endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": os.environ["API_KEY"],
            "client_secret": os.environ["API_SECRET"],
        }
        response = requests.post(endpoint, headers=header, data=body)

        return response.json()["access_token"]

    def get_offers(self, **kwargs):
        endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {key: value for key, value in kwargs.items()}
        params['nonStop'] = 'true'
        params['adults'] = 1
        params['currencyCode'] = 'USD'
        params['max'] = 10

        response = requests.get(endpoint, params=params, headers=header)
        print(response.json())
