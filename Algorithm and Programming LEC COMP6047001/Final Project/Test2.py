import curses
from curses import wrapper

def main(stdscr):
    stdscr.border()
    stdscr.addstr(1, 1, " _______   _______             _______   _______             _______                                   _______      _______             _______")
    stdscr.addstr(2, 1, "|         |       |  |\\    |  |         |       |     /\\        |     |       |  |             /\\         |     O  |       |  |\\    |  |          |")
    stdscr.addstr(3, 1, "|         |       |  | \\   |  |   ___   |_______|    /  \\       |     |       |  |            /  \\        |     |  |       |  | \\   |  |_______   |")
    stdscr.addstr(4, 1, "|         |       |  |  \\  |  |  |   |  |\\          /____\\      |     |       |  |           /____\\       |     |  |       |  |  \\  |          |  |")
    stdscr.addstr(5, 1, "|         |       |  |   \\ |  |      |  |  \\       /      \\     |     |       |  |          /      \\      |     |  |       |  |   \\ |          |  |")
    stdscr.addstr(6, 1, "|_______  |_______|  |    \\|  |______|  |    \\    /        \\    |     |_______|  |_______  /        \\     |     |  |_______|  |    \\|   _______|  O")

    while True:
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)