# Cailan White 2025
# Simple script to get weather for Edinburgh

import requests
import json

api_key = ''
post_code = 'EH11 2JW'

url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={post_code}&aqi=no'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Success")
else:
    print(f"Error: {response.status_code}")



