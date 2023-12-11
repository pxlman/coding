import curses 
from curses.textpad import Textbox, rectangle

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    win = curses.newwin(8,8,3,3)
    rectangle(stdscr,2,2,12,12)
    stdscr.border(curses.COLOR_BLUE)
    stdscr.refresh()
    tbox = Textbox(win)
    tbox.edit()
    text = tbox.gather().replace("\n","")
    stdscr.addstr(15,15,text)
    stdscr.move(0,0)
    stdscr.getch()

curses.wrapper(main)
