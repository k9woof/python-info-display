# python-info-display
Morning information to run off of an rpi/pc at login

This is largely for practice at manipulating data from several APIs.

6 basic information scripts which manipulate and display data from 4 apis:
-bustimes.py 
-weather.py
-stocks.py
-dailyverse.py
-news.py
-systeminfo.py

These are then displayed in a terminal GUI in display-script.py
display-script.py is designed to be ran at login in an RPI's terminal (for example on a Pi Zero 2 W with Raspbian Lite)

Dependencies:
-requests
-polygon
-newsapi