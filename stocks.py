# Cailan White
# Simple script to get stocks info

import requests
import json
import argparse
from polygon import RESTClient
from datetime import datetime, timedelta

def get_stocks_data(api_key):
    client = RESTClient(api_key)
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    if client:
        stock_data = client.get_grouped_daily_aggs(
            yesterday_str, 
            adjusted = "true"
        )
        return stock_data
    else:
        print("Polygon connection failed")

def get_stocks_lines(data):
    

def print_stocks(data):
    

def main():
    # stocks args
    parser = argparse.ArgumentParser(description="stocks")
    parser.add_argument('api_key', type=str, help='api_key')
    args = parser.parse_args()

    data = get_stocks_data(args.api_key)

    if data:
        print_stocks(data)
    else:
        print("Error getting data from the polygon API")

if __name__ == '__main__':
    main()