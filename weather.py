# Cailan White 2025
# Simple script to get weather for a given post code

import requests
import json
import argparse

#testing connection
def testConnection(api_key, post_code):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={post_code}&aqi=no'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")


def printData(data):
    print(data)

def main():
    parser = argparse.ArgumentParser(description="weather")
    parser.add_argument('api_key', type=str, help='api_key')
    parser.add_argument('post_code', type=str, help='post code')
    args = parser.parse_args()

    data = testConnection(args.api_key, args.post_code)

    if data:
        printData(data)

if __name__ == '__main__':
    main()
