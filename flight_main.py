#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# Import libraries
from data_manager import DataManager
from flight_search import FlightSearch


# Initialize classes
dm = DataManager()
fs = FlightSearch()

def main():
    sheet_data = dm.make_get_request()
    check_iata_codes(sheet_data)
    dm.iata_put_request(sheet_data)
    flight_details = fs.search_for_flight(sheet_data)
    cheaper_flights = compare_prices(sheet_data, flight_details)
    print(cheaper_flights)

def check_iata_codes(spreadsheet:dict) ->None:
    for data in spreadsheet:
        if data["iataCode"] == "":
            city = data["city"]
            iata_code = fs.get_iata_codes(city)
            data["iataCode"] = iata_code


def compare_prices(sheet_data:list, flight_details:list):
    # get google sheet data price
    lowest_price = {entry["iataCode"]: entry["lowestPrice"] for entry in sheet_data}
    
    # Filter the flights from flight_details that are cheaper than the lowest price
    cheaper_flights = []

    for flight in flight_details:
        current_destination = flight["destination"]

        #Get lowest prices threshold for destination
        threshold_price = lowest_price.get(current_destination, float("inf"))

        if flight["price"] < threshold_price:
            cheaper_flights.append(flight)


def send_sms():
    pass


if __name__ == "__main__":
    main()
