# Cailan White
# Simple script to get stocks info

import requests
import json
import argparse
from polygon import RESTClient
from datetime import datetime, timedelta

# get stocks data from polygon api
def get_stocks_data(api_key):
    client = RESTClient(api_key)
    yesterday = datetime.now() - timedelta(days=3)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    if client:
        stock_data = client.get_grouped_daily_aggs(
            yesterday_str,
            adjusted = "true"
        )
        return stock_data
    else:
        print("Polygon connection failed")

# get stocks open & close from 3 days ago as lines
def get_stocks_lines(data, symbols):
    stock_lines = []
    needed_symbols = filter_stocks(data, symbols)
    for stock in needed_symbols:
        stock_lines.append(f"{stock.ticker} - > Open: {stock.high}, Close: {stock.close}")
    return stock_lines

# filter stocks to only get the ones wanted
def filter_stocks(data, symbols):
    symbol_set = set(symbols)
    needed_symbols = []
    for stock in data:
        if stock.ticker in symbol_set:
            needed_symbols.append(stock)
    return needed_symbols

# print stocks open and close
def print_stocks(data, symbols):
    print("Previous day open & close::")
    needed_symbols = filter_stocks(data, symbols)
    for stock in needed_symbols:
        print(f"{stock.ticker} - > Open: {stock.high}, Close: {stock.close}")

def main():
    # stocks args
    parser = argparse.ArgumentParser(description="stocks")
    parser.add_argument('api_key', type=str, help='api_key')
    parser.add_argument('symbols', nargs='+', help='symbols')
    args = parser.parse_args()

    data = get_stocks_data(args.api_key)

    if data:
        print_stocks(data, args.symbols)
        
    else:
        print("Error getting data from the polygon API")

if __name__ == '__main__':
    main()