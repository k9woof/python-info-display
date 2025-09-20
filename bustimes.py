# Cailan White 2025
# Simple script to pull latest bus times from tfe bus times api

import requests 
import argparse
import json
from datetime import datetime, timedelta

# getting bus times
def get_bus_data(stop):
    url = f'https://tfe-opendata.com/api/v1/live_bus_times/{stop}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")

def bus_lines(data, routeNumbers):
    service_rows = []
    for route in data:
        if route['routeName'] in routeNumbers:
            for departure in route['departures']:
                departure_time_unix = departure['departureTimeUnix']
                departure_time = datetime.fromtimestamp(departure_time_unix)
                actual_time = departure_time - timedelta(hours = 2)
                formatted_time= actual_time.strftime('%H:%M')
                service_rows.append((route['routeName'], departure['destination'], formatted_time))

    service_rows.sort(key=lambda x: x[2]) 
    return service_rows

#printing bus data
def print_bus_data(routeNumbers, data): 
    service_rows = []

    #header
    headers = ["Number", "Destination", "Departure Time"]
    header_row = f"{headers[0]: <10}{headers[1]:<20}{headers[2]:<15}"
    print(header_row)
    print("-" * len(header_row))

    #services
    service_rows = bus_lines(data, routeNumbers)
    for service in service_rows:
        print(f"{service[0]:<10}{service[1]:<20}{service[2]:<15}")

def get_bus_lines(routeNumbers, data):
    service_rows = bus_lines(data, routeNumbers)
    return [f"{route:<10} {destination:<20} {time:<15}" for route, destination, time in service_rows]

def main():

    # bus stop & services args
    parser = argparse.ArgumentParser(description="live bus times")
    parser.add_argument('stop', type=int, help='bus stop')
    parser.add_argument('services', nargs='+', help='services')
    args = parser.parse_args()
    data = get_bus_data(args.stop)

    if data:
        print_bus_data(args.services, data)
    else:
        print("Error getting data from TFE API")

if __name__ == "__main__":
    main()