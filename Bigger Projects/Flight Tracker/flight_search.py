import requests
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        access_token = self.get_token()
        self.header = {
            "Authorization": f"Bearer {access_token}"
       }

    def get_flights(self, city):
        params = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(self.endpoint, params=params, headers=self.header)
        try:
            return response.json()["data"][0]["iataCode"]
        except IndexError:
            return "N/A"
        except KeyError:
            return "Not Found"

    def get_token(self):
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