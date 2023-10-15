# Import libraries
import requests

# API Required: Sheety
#This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self) -> None:
        self.sheety_api_endpoint = "insert your data google docs spreadsheet entry here VIA SHEETY"
    
    def make_get_request(self):
        self.sheety_get_response = requests.get(url=self.sheety_api_endpoint)
        self.sheety_get_response.raise_for_status()
        data = self.sheety_get_response.json()   
        return data["prices"]  

    def iata_put_request(self, spreadsheet):
        self.spreadsheet = spreadsheet
        
        for entry in self.spreadsheet:
            row_id = entry["id"]
            endpoint = f"{self.sheety_api_endpoint}/{row_id}"
            payload = {
                "price" : {
                    "iataCode" : entry["iataCode"]
                }
            }
            
            response = requests.put(endpoint, json=payload)
            if response.status_code != 200: 
                print(f"Error updating row {row_id}. Status code: {response.status_code}")
                print(response.text)  



