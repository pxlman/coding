import curses
# from curses import wrapper

def main(stdscr):
    # Colors
    curses.init_pair(1,curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    mag_b = curses.color_pair(1)
    # Screen clearing
    stdscr.clear()
    stdscr.refresh()
    # Pad
    pad = curses.newpad(100,100)
    pad.addstr(0,0,"hello world",mag_b)
    pad.addstr(1,1,"hello world",mag_b)
    pad.addstr(2,2,"hello world",mag_b)
    # Pad refreshing
    pad.refresh(2,2,0,0,5,5)
    # Screen refrehing
    stdscr.getch()

curses.wrapper(main)
