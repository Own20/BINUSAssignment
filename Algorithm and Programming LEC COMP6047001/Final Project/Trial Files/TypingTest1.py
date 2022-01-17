import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
	stdscr.clear()
	stdscr.border()
	stdscr.addstr(1, 25, "                       _______             _______   _______                          _______     _______   _______")
	stdscr.addstr(2, 25, "\\        /\\        /  |         |         |         |       |      /\\        /\\      |               |     |       |")
	stdscr.addstr(3, 25, " \\      /  \\      /   |_______  |         |         |       |     /  \\      /  \\     |_______        |     |       |")
	stdscr.addstr(4, 25, "  \\    /    \\    /    |         |         |         |       |    /    \\    /    \\    |               |     |       |")
	stdscr.addstr(5, 25, "   \\  /      \\  /     |         |         |         |       |   /      \\  /      \\   |               |     |       |")
	stdscr.addstr(6, 25, "    \\/        \\/      |_______  |_______  |_______  |_______|  /        \\/        \\  |_______        |     |_______|")
	stdscr.addstr(8, 28, "              _______             _______                        _______  _______            _______    _______")
	stdscr.addstr(9, 28, "|         o  |         |       |     |     |\\    |  o  |\\    |  |            |     \\     /  |       |  |")
	stdscr.addstr(10, 28, "|         |  |   ___   |_______|     |     | \\   |  |  | \\   |  |   ___      |      \\   /   |       |  |_______")
	stdscr.addstr(11, 28, "|         |  |  |   |  |       |     |     |  \\  |  |  |  \\  |  |  |   |     |       \\ /    |_______|  |")
	stdscr.addstr(12, 28, "|         |  |      |  |       |     |     |   \\ |  |  |   \\ |  |      |     |        |     |          |")
	stdscr.addstr(13, 28, "|_______  |  |______|  |       |     |     |    \\|  |  |    \\|  |______|     |        |     |          |_______")
	stdscr.addstr(15, 69, "Press any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

def display_text(stdscr, target, current, wpm=0, time=0):
	stdscr.border()
	stdscr.addstr(1, 28, "              _______             _______                        _______  _______            _______    _______")
	stdscr.addstr(2, 28, "|         o  |         |       |     |     |\\    |  o  |\\    |  |            |     \\     /  |       |  |")
	stdscr.addstr(3, 28, "|         |  |   ___   |_______|     |     | \\   |  |  | \\   |  |   ___      |      \\   /   |       |  |_______")
	stdscr.addstr(4, 28, "|         |  |  |   |  |       |     |     |  \\  |  |  |  \\  |  |  |   |     |       \\ /    |_______|  |")
	stdscr.addstr(5, 28, "|         |  |      |  |       |     |     |   \\ |  |  |   \\ |  |      |     |        |     |          |")
	stdscr.addstr(6, 28, "|_______  |  |______|  |       |     |     |    \\|  |  |    \\|  |______|     |        |     |          |_______")
	stdscr.addstr(9, 10, target)
	stdscr.addstr(13, 50, f"WPM: {wpm}")
	stdscr.addstr(13, 100, f"Time: {round(time, 1)}")

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(9, 10+i, char, color)

def load_text():
	with open("Text.txt", "r") as f:
		lines = f.readlines()
		return random.choice(lines).strip()

def wpm_test(stdscr):
	target_text = load_text()
	current_text = []
	wpm = 0
	start_time = 0
	start_time = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm, time_elapsed)
		stdscr.refresh()

		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(stdscr)
	while True:
		wpm_test(stdscr)
		stdscr.addstr(11, 54, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)