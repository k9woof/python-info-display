# Cailan White
# Terminal GUI to run at login

import curses
import weather
import bustimes
import argparse
from config import weather_api_key, weather_post_code, stop_number, services

# drawing boxes
def draw_box(win, title, lines):
    win.box()
    max_y, max_x = win.getmaxyx()
    win.addstr(0, 2, f" {title} ")
    for i, line in enumerate(lines):
        if i + 1 < max_y - 1:
            win.addstr(i + 1, 2, line[:max_x - 4])
    win.refresh()

def format_bus_data(data):
    return [f"{route:<10} {destination:<20} {time:<15}" for route, destination, time in data]

def dashboard(stdscr):
    w_api_key = weather_api_key
    postcode = weather_post_code
    bus_stop_number = stop_number
    bus_routes = services

    curses.curs_set(0)
    stdscr.clear()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    height, width = stdscr.getmaxyx()
    height //=3
    width //=2

    # weather box   
    weather_win = curses.newwin(height, width-5, 0, 0)
    weather_data = weather.testConnection(w_api_key, postcode)
    weather_lines = weather.getWeatherlines(weather_data)

    # bus box
    bus_win = curses.newwin(height, width-5, 0, width+5)
    bus_data = bustimes.testConnection(bus_stop_number)
    
    bus_lines = bustimes.getBusLines(bus_routes, bus_data)
    formatted_bus_lines = format_bus_data(bus_lines)

    stdscr.refresh()

    # divider
    divider_x = width
    for y in range(height*3):
        stdscr.addch(y, divider_x, curses.ACS_CKBOARD)
    draw_box(weather_win, "Weather", weather_lines)
    draw_box(bus_win, "Bus Times", formatted_bus_lines)

    # exit
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

def run_dashboard():
    curses.wrapper(dashboard)

if __name__ == "__main__":
    run_dashboard()
