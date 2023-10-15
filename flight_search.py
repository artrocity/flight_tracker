# Import libraries
import requests
import pytz

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class FlightSearch:
    def __init__(self) -> None:
        self.fly_from = "SET YOUR DEPARTURE AIRPORT/AIRPORTS"
        self.set_time()
        self.API_KEY = "SET YOUR ENVIRONMENT VARIABLE API KEY HERE"

    def set_time(self):
        tomorrow = (datetime.today() + timedelta(days=1))
        self.date_tomorrow = tomorrow.strftime("%d/%m/%Y")

        six_months = tomorrow + relativedelta(months=6)
        self.date_six_months = six_months.strftime("%d/%m/%Y")

    def get_iata_codes(self, city):
        self.city = city
        self.search_endpoint = "https://tequila-api.kiwi.com/locations/query"

        headers = {
            "apikey" : self.API_KEY
        }

        params = {
            "term" : self.city,
            "location_types" : "airport",
            "limit" : 1
        }

        iata_response = requests.get(self.search_endpoint, headers=headers, params=params)
        data = iata_response.json()

        if data["locations"]:
            iata_code = data["locations"][0]["id"]
            return iata_code
        else:
            return None
        
    def format_times(self, iso_time):
        # Parse
        dt = datetime.fromisoformat(iso_time.replace("z", "+00:00"))

        # Set the timezone
        local_timezone = pytz.timezone("US/Central")
        local_dt = dt.astimezone(local_timezone)

        # Format the Date and Time
        formatted_date = local_dt.strftime("%Y-%m-%d")
        formatted_time = local_dt.strftime(":%H:%M %p")

        return formatted_date, formatted_time
       
    def search_for_flight(self, data):
        tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"
        header = {
            "apikey" : self.API_KEY
        }

        for entry in data:
            iata_code = entry["iataCode"]
            query = {
                "fly_from" : self.fly_from,
                "fly_to" : iata_code,
                "date_from" : self.date_tomorrow,
                "date_to" : self.date_six_months,
                "nights_in_dst_from" : 3,
                "nights_in_dst_to" : 10,
                "one_for_city" : 1,
                "curr" : "USD"
            }

            response = requests.get(tequila_endpoint, headers=header, params=query)
            response.raise_for_status()
            flight_data = response.json()["data"]

            if flight_data:
                first_flight = flight_data[0]
                fly_from = first_flight["flyFrom"]
                fly_to = first_flight["flyTo"]
                night_stay = first_flight["nightsInDest"]
                price = first_flight["price"]
                departure = first_flight["local_departure"]

                formatted_date, formatted_time = self.format_times(departure)
                print(f"Found 1 flight, leaving {fly_from}, on {formatted_date} @ {formatted_time} flying to {fly_to} for {night_stay} nights for ${price}.")
            

        
