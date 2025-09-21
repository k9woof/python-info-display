# Cailan White 2025
# Simple news feed script 

import requests
import json
import argparse
from newsapi import NewsApiClient

# get bbc-news data from newsapi
def get_news_data(api_key):
    client = NewsApiClient(api_key)
    if client:
        news_data = client.get_top_headlines(
            sources='bbc-news'
        )
        return news_data
    else:
        print("NewsAPI connection failed")

# get news headlines as lines
def get_news_lines(data):
    news_lines = []
    articles = data['articles']
    for article in articles:
        news_lines.append(article['title'])
    return news_lines

# print bbc-news headlines
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