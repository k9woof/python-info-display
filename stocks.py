# Cailan White
# Simple script to get my stocks

import requests
import json

def get_stocks_data(api_key):
    url = ''
    response = requests.get(url)

    if response.status_code == 200:
        stocks = response.json()
        return stocks
    else:
        print(f"Error: {response.status_code}")

def get_stocks_lines():
    print("hello")

def print_stocks():
    print("Hello")

def main():
    stocks = get_stocks_data()

    if stocks:
        print_stocks(stocks)
    else:
        print("Error getting data from the stocks API")

if __name__ == '__main__':
    main()