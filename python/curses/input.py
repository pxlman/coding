import curses
'''
down 258
up 259
left 260
right 261
space 32
enter 10
'''
down  = 258
up    = 259
left  = 260
right = 261
space = 32
enter = 10
q = 113
def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.nodelay(True)
    y = int((curses.LINES - 1) / 2)
    x = int((curses.COLS - 1) / 2)
    stdscr.addstr(y,x,"0")
    while True:
        try:
            key = stdscr.getch()
        except:
            key = None
        if key == q:
            break
        elif key == up and y > 0:
            y -= 1
        elif key == down and y < curses.LINES - 1:
            y += 1
        elif key == left and x > 0:
            x -= 1
        elif key == right and x < curses.COLS - 1:
            x += 1
        # stdscr.clear()
        # stdscr.refresh()
        stdscr.addstr(y,x,"0")

curses.wrapper(main)
