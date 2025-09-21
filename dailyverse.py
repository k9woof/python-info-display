# Cailan White
# Simple script to get a daily bible verse

import requests
import json

# getting daily verse from ourmanna api
def get_bible_verse():
    url = ' https://beta.ourmanna.com/api/v1/get?format=json&order=daily"'
    response = requests.get(url)
    if response.status_code == 200:
        bible_verse = response.json()
        return bible_verse
    else:
        print(f"Error: {response.status_code}")

# getting daily verse as a line
def get_bible_lines(daily_verse):
    verse = daily_verse['verse']
    details = verse['details']
    text = details['text']
    chapter_verse = details['reference']
    return f"'{text}'\n {chapter_verse}"

# printing daily-verse
def print_bible_verse(daily_verse):
    verse = daily_verse['verse']
    details = verse['details']
    text = details['text']
    chapter_verse = details['reference']
    print("Daily Bible verse:\n")
    print(f"'{text}'\n {chapter_verse}")

def main():
    daily_verse = get_bible_verse()

    if daily_verse:
        print_bible_verse(daily_verse)
    else:
        print("Error getting data from the Bible verse API")

if __name__ == '__main__':
    main()