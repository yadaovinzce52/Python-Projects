#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import requests
import os
from dotenv import load_dotenv
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()

dataManager = DataManager()
sheet_data = dataManager.get_data()

# pprint(sheet_data)

flightSearch = FlightSearch()
for data in sheet_data:
    if not data["iataCode"]:
        iataCode = flightSearch.get_flights(data["city"])
        dataManager.update_data(data, iataCode)
