import curses
#curses module
from curses import wrapper
#initialize curses module, take over terminal to run different commands, after finish restore terminal back

def main(stdscr):
#stdscr = standard output to write stuff to the screen
    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    #create a pair for foreground and background color
    #parameter: (ID, foreground color, background color)

    stdscr.clear()
    #clears the entire screen

    # stdscr.addstr("Hello world!")
    # #similiar to print statement / output the text
    # stdscr.addstr("Hello world!", curses.color_pair(1))
    # #to use - reference one of the pairs with the ID in the brackets
    stdscr.addstr(1, 5, "Hello world!", curses.color_pair(1))
    #to specify the row and column position where the text start
    stdscr.addstr(1, 0, "Hello world!", curses.color_pair(1))
    #the second will overlap the first text

    stdscr.refresh()
    #refresh the screen
    # stdscr.getkey()
    # #wait for the user to type something, so it won't show and close immediately - to keep track what the user type
    key = stdscr.getkey()
    print(key)
    #if hit any key, the key will show up

wrapper(main)
#passing the main function to the wrapper function - to call main function while initializing things related to curses module