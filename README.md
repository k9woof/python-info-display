# python-info-display
Morning information to run off of an rpi at login

4 basic information scripts which manipulate and display data from 4 apis:
-bus-times.py 
-weather.py
-timetable.py
-daily-verse.py

These are then displayed in a wonderful terminal GUI in display-script.py
Display-script.py is designed to be ran at login in an RPI's terminal (for example on a Pi Zero 2 W with Raspbian OS Lite)

How to's:

How to run bus-times.py?

1. In a terminal, navigate to the folder where bus-times.py is. For example if it were in downloads, type cd Downloads.
2. Then type python3 bus-times.py stop services (replace stop & services with actual values). e.g python3 bus-times.py 36236498 34

How to run weather.py?

1. In a terminal, navigate to the folder where bus-times.py is. For example if it were in downloads, type cd Downloads.
2. Then type python3 weather.py api_key post_code (replace api_key & post_code with actual values). e.g python3 bus-times.py apiKey 'EH14 4AS'