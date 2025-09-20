# Cailan White 2025
# Simple script to get weather for a given post code

import requests
import json
import argparse

#testing connection
def testConnection(api_key, post_code):
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={post_code}&days=1&aqi=no&alerts=no'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")


# printing current weather
def printData(data):
    location = data['location']
    forecast_weather = data['forecast']
    forecast = forecast_weather['forecastday'][0]
    todays_forecast = forecast['day']
    condition = todays_forecast['condition']

    print(f"Todays's weather for {location['name']}:\n")
    print(f"Summary: {condition['text']}")
    print(f"Average Temperature: {todays_forecast['avgtemp_c']}°C")
    print(f"Max/Min Temperature: {todays_forecast['maxtemp_c']}°C/{todays_forecast['mintemp_c']}°C")
    print(f"Wind speed: {todays_forecast['maxwind_mph']} mph")
    print(f"Chance of rain today: {todays_forecast['daily_chance_of_rain']}%")

def getWeatherlines(data):
    forecast_weather = data['forecast']
    forecast = forecast_weather['forecastday'][0]
    todays_forecast = forecast['day']
    condition = todays_forecast['condition']

    return [
        f"Summary: {condition['text']}",
        f"Average Temperature: {todays_forecast['avgtemp_c']}°C",
        f"Max/Min Temperature: {todays_forecast['maxtemp_c']}°C/{todays_forecast['mintemp_c']}°C",
        f"Wind speed: {todays_forecast['maxwind_mph']} mph",
        f"Chance of rain today: {todays_forecast['daily_chance_of_rain']}%"
    ]

def main():

    # weather args
    parser = argparse.ArgumentParser(description="weather")
    parser.add_argument('api_key', type=str, help='api_key')
    parser.add_argument('post_code', type=str, help='post code')
    args = parser.parse_args()

    data = testConnection(args.api_key, args.post_code)

    if data:
        printData(data)
    else:
        print("Error getting data from the weather API")

if __name__ == '__main__':
    main()

