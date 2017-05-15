import webbrowser
import time


def take_break():
    total_breaks = 5
    count = 0
    while count < total_breaks:
        webbrowser.open('https://www.youtube.com/watch?v=fBdRI-1mmX4')
        time.sleep(1500)
        count += 1

take_break()