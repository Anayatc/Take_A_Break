import webbrowser
import time


def take_break():
    total_breaks = 3
    count = 0
    while count < total_breaks:
        webbrowser.open('https://www.youtube.com/watch?v=fBdRI-1mmX4')
        time.sleep(10)