# Summary
    Uses Python to track a list of flight destinations via a spreadsheet and will update you when a flight goes on sale below a targeted(user set) value.  

## Libraries/Modules
    import requests
    import pytz
    
    from datetime import datetime, timedelta
    from dateutil.relativedelta import relativedelta
    from twilio.rest import Client - Future implementation to notify you via text message when a flight drops below a certain dollar value (could also use email via smtp)


### Usage
    In order to use this app for your own purposes, you will need to change a few items.
      -flight_search.py
        - In the FlightSearch class, you will need to update the self.fly_from to be your departure airport, use the IATA code.
        - Update the self.API_KEY (This will need to be the key you are given by tequila by Kiwi or another similar flight search API of your choosing
        - USD, you can change to whichever currency of your liking
        - In the DataManager class in data_manager.py you will need to change:
                - the self.sheety_api_endpoint to the endpoint of your specific "Sheety dashboard google spreadsheet"
        - Optional changes:
            - In the search_for_flight method, you can change certain search parameters to be sent as the payload to the API such as: 
                - Date From
                - Date To
                - Nights in destination
                - One for City (this limites the results to just one flight per city and chooses the cheapest flight by default if set to 1)
                - curr
        
 #### Design implementations
    - Currently this design of the program will pull from the Kiwi flight search rest api as well as your sheety spreadsheet and use a get request to obtainall relevant flight data from your spreadsheet.
      Then, it uses the data to find flights based on the parameters set in the payload to find the cheapest flights leaving your departure airport to all destinations listed in the spreadsheet and will find the
      cheapest flight therein. After locating all of the flights, the data is parsed and then simply printed to the console. 
    
    - Future Design implementations: 
          - I will either have this program use a text messaging sms feature that alerts you when a price is found below a certain threshold that is user defined or use the data to create a series of charts on a website to show changes.
            Right now, im leaning towards the former. 

##### TODO
    - Create a website with chart flows, that show the current data in a graphical format with changes and a history search or SMS notification feature
    - Update the python file with all the necessary documentation for each function via the "Docstring Method"



