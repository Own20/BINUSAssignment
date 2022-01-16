import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
	stdscr.clear()
	stdscr.border()
	stdscr.addstr(1, 31, "                        _______             _______   _______                          _______   |")
	stdscr.addstr(2, 32, "\\        /\\        /  |         |         |         |       |      /\\        /\\      |          |")
	stdscr.addstr(3, 33, "\\      /  \\      /   |_______  |         |         |       |     /  \\      /  \\     |_______   |")
	stdscr.addstr(4, 34, "\\    /    \\    /    |         |         |         |       |    /    \\    /    \\    |          |")
	stdscr.addstr(5, 35, "\\  /      \\  /     |         |         |         |       |   /      \\  /      \\   |          |")
	stdscr.addstr(6, 36, "\\/        \\/      |_______  |_______  |_______  |_______|  /        \\/        \\  |_______   o")
	stdscr.addstr(7, 60, "To Speed Typing Test!")
	stdscr.addstr(8, 60, "Press any key to begin!")
	stdscr.refresh()
	while True:
		c = stdscr.getch()
		if c == ord('\n'):
			break

def display_text(stdscr, target, current, wpm=0, time=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}")
	stdscr.addstr(1, 10, f"Time: {round(time, 1)}")

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(0, i, char, color)

def load_text():
	with open("Text.txt", "r") as f:
		lines = f.readlines()
		return random.choice(lines).strip()

def wpm_test(stdscr):
	target_text = load_text()
	current_text = []
	wpm = 0
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
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)