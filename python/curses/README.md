# Starting

```py
import curses
def main(stdscr):
    # Clears the screen from any char
    stdscr.clear()
    # Add some string
    stdscr.addstr(...)
    # Refreshes the screen to show the stuff in live time
    stdscr.refresh()
curses.wrapper(main)
```

# Atributes and colors

## Atributes

```py
stdscr.addstr(y,x,"blabla",curses.A_EXAMPLE)
# EXAMPLE can be
# BOLD, ITALIC, STANDOUT, REVERSE, NORMAL
```

## Colors

###

```py
curses.init_pair(i,curses.COLOR_EXAMPLE,curses,COLOR_EXAMPLE)# i,fg,bg
# EXAMPLE can be
# RED, MAGENTA, BLACK, BLUE ..
fg_bg = curses.color_pair(i)
stdscr.addstr(y,x,"blabla", fg_bg)
```

## Combining color and atrib

```py
stdscr.addstr(y,x,"blabla",curses.COLOR_EXAMPLE | curses.A_EXAMPLE)
```

# Windows and pading

## Screen limit

```py
max_rows = curses.LINES - 1
max_cols = curses.COLS - 1

```

## Windows

```py
win = curses.newwin(height, width,
begin_y, begin_x)
win.addstr(...)
win.refresh()
```

## Pads

```py
pad = curses.newpad(prect_row,`HelpChoosingContent`
                    prect_col,`With respect to pad`
                    s_row,`start pos`
                    s_col,`with respect to win`
                    e_row,`end pos`
                    e_col)`with respect to win`

```

# Input and text boxes

## User input

```py
key = curses.getch() #return key num
'''
down 258
up 259
left 260
right 261
space 32
enter 10
and so on ...
'''
key = curses.getkey() #return key name
```

## Rectangle

```py
curses.textpad.rectangle(stdscr,y_spos,x_spos,y_epos,y_epos)#epos: end pos, spos: start pos
```

## Text box

```py
tbox = curses.textpad.Textbox(curses.newwin(...))
```

## Cursor loc

```py
stdscr.move(y,x)
```

## No delay

No delay while taking input from user, just complete the code without waiting.
use:

```py
stdscr.nodelay(True)
```

[curses doc](https://docs.python.org/3/library/curses.html#curses.window.refresh)
