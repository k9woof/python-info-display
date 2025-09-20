# Cailan White
# Simple script to get my timetable

import requests
import json

def get_timetable_data():
    url = ''
    response = requests.get(url)

    if response.status_code == 200:
        timetable = response.json()
        return timetable
    else:
        print(f"Error: {response.status_code}")

def get_timetable_lines():
    print("hello")

def print_timetable():
    print("Hello")

def main():
    timetable = get_timetable_data()

    if timetable:
        print_timetable(timetable)
    else:
        print("Error getting data from the weather API")

if __name__ == '__main__':
    main()