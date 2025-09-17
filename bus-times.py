import requests 
import json
from datetime import datetime, timedelta

# St Michaels Church
stop = 36236498
url = f'https://tfe-opendata.com/api/v1/live_bus_times/{stop}'

response = requests.get(url)

#testing connection
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")

#printing bus data
def printData(routeNumbers, data): 
    service_rows = []

    #header
    headers = ["Number", "Destination", "Departure Time"]
    header_row = f"{headers[0]: <10}{headers[1]:<20}{headers[2]:<15}"
    print(header_row)
    print("-" * len(header_row))

    #services
    for route in data:
        if route['routeName'] in routeNumbers:
            for departure in route['departures']:
                departure_time_unix = departure['departureTimeUnix']
                departure_time = datetime.fromtimestamp(departure_time_unix)
                actual_time = departure_time - timedelta(hours = 2)
                formatted_time= actual_time.strftime('%H:%M:%S')
                service_rows.append((route['routeName'], departure['destination'], formatted_time))

    service_rows.sort(key=lambda x: x[2]) 
    for service in service_rows:
        print(f"{service[0]:<10}{service[1]:<20}{service[2]:<15}")

printData(['34', '35'], data)
