# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt

load_dotenv()

ORIGIN = 'TLH'

dataManager = DataManager()
sheet_data = dataManager.get_data()

# pprint(sheet_data)

flightSearch = FlightSearch()
for data in sheet_data:
    if not data["iataCode"]:
        iataCode = flightSearch.get_flights(data["city"])
        dataManager.update_data(data['id'], iataCode)

sheet_data = dataManager.get_data()

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_month_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))


for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flightSearch.get_offers(
        originLocationCode=ORIGIN,
        destinationLocationCode=destination['iataCode'],
        departureDate=tomorrow.strftime("%Y-%m-%d"),
        returnDate=six_month_from_today.strftime("%Y-%m-%d"),
        nonStop='true',
        adults=1,
        currencyCode='USD',
        max=10
    )
