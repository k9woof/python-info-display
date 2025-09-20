# Cailan White
# Simple script to get stocks info

import requests
import json
import argparse
from polygon import RESTClient

def get_stocks_data(api_key, symbols):
    client = RESTClient(api_key)
    str_symbols = ','.join(symbols)
    if client:
        stock_data = client.get_ticker_details(str_symbols)
        return stock_data
    else:
        print("Polygon connection failed")

def get_stocks_lines():
    print("hello")

def print_stocks():
    print("Hello")

def main():
    # stocks args
    parser = argparse.ArgumentParser(description="stocks")
    parser.add_argument('api_key', type=str, help='api_key')
    parser.add_argument('symbols', nargs='+', help='stock symbols')
    args = parser.parse_args()

    data = get_stocks_data(args.api_key, args.symbols)

    if data:
        print_stocks()
    else:
        print("Error getting data from the polygon API")

if __name__ == '__main__':
    main()