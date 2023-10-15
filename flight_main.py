# Import libraries
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch


# Initialize classes
dm = DataManager()
fs = FlightSearch()

def main():
    sheet_data = dm.make_get_request()
    check_iata_codes(sheet_data)
    dm.iata_put_request(sheet_data)
    fs.search_for_flight(sheet_data)

def check_iata_codes(spreadsheet:dict) ->None:
    for data in spreadsheet:
        if data["iataCode"] == "":
            city = data["city"]
            iata_code = fs.get_iata_codes(city)
            data["iataCode"] = iata_code
    
def compare_prices():
    # get google sheet data price
    # get current prices from search for flight
    # see if any of the prices are less than desired price
    # if they are, send SMS with flight details
    pass

def send_sms():
    pass

if __name__ == "__main__":
    main()
