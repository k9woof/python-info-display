# Cailan White
# Terminal GUI to run at login/run

import curses
import weather
import bustimes
import dailyverse
import stocks
import news
import systeminfo
import textwrap
from config import weather_api_key, weather_post_code, stop_number, services, stocks_api_key, news_api_key, symbols

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

# gui
def dashboard(stdscr):
    w_api_key = weather_api_key
    postcode = weather_post_code
    bus_stop_number = stop_number
    bus_routes = services
    s_api_key = stocks_api_key
    n_api_key = news_api_key

    curses.curs_set(0)
    stdscr.clear()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

    height, width = stdscr.getmaxyx()
    row_height = height // 3
    col_width = width // 2

    # weather box   
    weather_win = curses.newwin(row_height, col_width, 0, 0)
    weather_data = weather.get_weather_data(w_api_key, postcode)
    weather_lines = weather.get_weather_lines(weather_data)

    # bus box
    bus_win = curses.newwin(row_height, col_width, 0, col_width)
    bus_data = bustimes.get_bus_data(bus_stop_number)
    bus_lines = bustimes.get_bus_lines(bus_routes, bus_data)

    # bible-verse box
    bible_win = curses.newwin(row_height, col_width, row_height, 0)
    bible_verse = dailyverse.get_bible_verse()
    bible_lines = dailyverse.get_bible_lines(bible_verse)

    # stocks box
    stocks_win = curses.newwin(row_height, col_width, row_height, col_width)
    stocks_data = stocks.get_stocks_data(s_api_key)
    stocks_lines = stocks.get_stocks_lines(stocks_data, symbols)

    # news box
    news_win = curses.newwin(row_height, col_width, row_height*2, 0)
    news_data = news.get_news_data(n_api_key)
    news_lines = news.get_news_lines(news_data)

    # systeminfo box
    system_info_win = curses.newwin(row_height, col_width, row_height*2, col_width)
    system_info_lines = systeminfo.get_system_info_lines()

    # exit
    stdscr.addstr(height -1,0, "Press q to exit")
    stdscr.refresh()

    # boxes
    draw_box(weather_win, "Weather", weather_lines)
    draw_box(bus_win, "Bus Times", bus_lines)
    draw_box(bible_win, "Bible-Verses", bible_lines)
    draw_box(stocks_win, "Stocks", stocks_lines)
    draw_box(news_win, "News", news_lines)
    draw_box(system_info_win, "System Info", system_info_lines)

    # exit
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

def run_dashboard():
    curses.wrapper(dashboard)

if __name__ == "__main__":
    run_dashboard()
