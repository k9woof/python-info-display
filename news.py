# Cailan White 2025
# Simple news feed script 

import requests
import json
import argparse
from newsapi import NewsApiClient

def get_news_data(api_key):
    client = NewsApiClient(api_key)
    if client:
        news_data = client.get_top_headlines(
            sources='bbc-news'
        )
        return news_data
    else:
        print("Polygon connection failed")

def get_news_lines(data):
    news_lines = []
    articles = data['articles']
    for article in articles:
        news_lines.append(article['title'])
    return news_lines

def print_news(data):
    articles = data['articles']
    print("Top BBC-News headlines")
    for article in articles:
        print(article['title'])

def main():
# stocks args
    parser = argparse.ArgumentParser(description="news")
    parser.add_argument('api_key', type=str, help='api_key')
    args = parser.parse_args()

    data = get_news_data(args.api_key)

    if data:
        print_news(data)
    else:
        print("Error getting data from the NewsApi API")

if __name__ == '__main__':
    main()