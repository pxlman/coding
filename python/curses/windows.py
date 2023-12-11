import curses
from curses import A_STANDOUT, wrapper
import time

def main(stdscr):
    stdscr.clear()
    # dim, normal, standout(highlighted), bold, italic
    curses.init_pair(1,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    mag_black = curses.color_pair(1)
    red_black = curses.color_pair(2)
    counter_win = curses.newwin(3,20,0,0)
    counter_win.clear()
    # counter_win.addstr(0,0,"Hello world", mag_black | curses.A_STANDOUT)
    # counter_win.addstr(2,0,"Hello world", curses.A_BOLD)
    pad = curses.newpad(100,100)
    for i in range(100):
        if i % 2 == 0:
            color = mag_black
            atrib = curses.A_STANDOUT
        else:
            color = red_black
            atrib = curses.A_BOLD
        counter_win.addstr(1,0,f"I is: {i}",color | atrib)
        pad.addstr(0,0,"this pad")
        pad.refresh(0,10,5,5,10,10)
        counter_win.refresh()
        time.sleep(0.5)
    stdscr.getch()

wrapper(main)
