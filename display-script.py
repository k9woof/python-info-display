# Cailan White
# Terminal GUI to run at login

import curses
import weather
import bustimes
import dailyverse
import timetable
import textwrap
from config import weather_api_key, weather_post_code, stop_number, services

# drawing boxes
def draw_box(win, title, lines):
    win.box()
    max_y, max_x = win.getmaxyx()
    win.addstr(0, 2, f" {title} ")
    if type(lines) == list:
        for i, line in enumerate(lines):
            if i + 1 < max_y - 1:
                win.addstr(i + 1, 2, line[:max_x - 4])
    else:
        wrapped_lines = textwrap.wrap(str(lines), width=max_x -4)
        for i, line in enumerate(wrapped_lines):
            if i + 1 < max_y - 1:
                win.addstr(i + 1, 2, line)
    win.refresh()

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
    weather_data = weather.get_weather_data(w_api_key, postcode)
    weather_lines = weather.get_weather_lines(weather_data)

    # bus box
    bus_win = curses.newwin(height, width-5, 0, width+5)
    bus_data = bustimes.get_bus_data(bus_stop_number)
    bus_lines = bustimes.get_bus_lines(bus_routes, bus_data)

    # bible-verse box
    bible_win = curses.newwin(height, width-5, height*2-10, 0)
    bible_verse = dailyverse.get_bible_verse()
    bible_lines = dailyverse.get_bible_lines(bible_verse)

    # timetable box
    timetable_win = curses.newwin(height, width-5, width+5)
    timetable_data = timetable.get_timetable_data()
    timetable_lines = timetable.get_timetable_lines(timetable_data)

    stdscr.addstr(height*3 ,0, "Press q to exit")
    stdscr.refresh()

    # divider
    divider_x = width
    for y in range(height*3):
        stdscr.addch(y, divider_x, curses.ACS_CKBOARD)
    draw_box(weather_win, "Weather", weather_lines)
    draw_box(bus_win, "Bus Times", bus_lines)
    draw_box(bible_win, "Bible-Verse", bible_lines)
    draw_box(timetable_win, "Timetable", timetable_lines)

    # exit
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

def run_dashboard():
    curses.wrapper(dashboard)

if __name__ == "__main__":
    run_dashboard()
