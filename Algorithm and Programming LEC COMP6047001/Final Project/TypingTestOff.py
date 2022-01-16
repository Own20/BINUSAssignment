import curses
from curses import wrapper
import time
import random


def start_screen(typetest):
	typetest.clear()
	typetest.border()
	typetest.addstr(1, 25, "                       _______             _______   _______                          _______     _______   _______")
	typetest.addstr(2, 25, "\\        /\\        /  |         |         |         |       |      /\\        /\\      |               |     |       |")
	typetest.addstr(3, 25, " \\      /  \\      /   |_______  |         |         |       |     /  \\      /  \\     |_______        |     |       |")
	typetest.addstr(4, 25, "  \\    /    \\    /    |         |         |         |       |    /    \\    /    \\    |               |     |       |")
	typetest.addstr(5, 25, "   \\  /      \\  /     |         |         |         |       |   /      \\  /      \\   |               |     |       |")
	typetest.addstr(6, 25, "    \\/        \\/      |_______  |_______  |_______  |_______|  /        \\/        \\  |_______        |     |_______|")
	typetest.addstr(8, 28, "              _______             _______                        _______  _______            _______    _______")
	typetest.addstr(9, 28, "|         O  |         |       |     |     |\\    |  O  |\\    |  |            |     \\     /  |       |  |")
	typetest.addstr(10, 28, "|         |  |   ___   |_______|     |     | \\   |  |  | \\   |  |   ___      |      \\   /   |       |  |_______")
	typetest.addstr(11, 28, "|         |  |  |   |  |       |     |     |  \\  |  |  |  \\  |  |  |   |     |       \\ /    |_______|  |")
	typetest.addstr(12, 28, "|         |  |      |  |       |     |     |   \\ |  |  |   \\ |  |      |     |        |     |          |")
	typetest.addstr(13, 28, "|_______  |  |______|  |       |     |     |    \\|  |  |    \\|  |______|     |        |     |          |_______")
	typetest.addstr(15, 50, "Speed Typing Test will be measeured with Words Per Minute (WPM)")
	typetest.addstr(17, 69, "Press ENTER to begin!")
	typetest.refresh()
	while True:
		c = typetest.getch()
		if c == ord('\n'):
			break


def display_text(typetest, target, current, wpm=0, time=0):
	typetest.border()
	typetest.addstr(1, 28, "              _______             _______                        _______  _______            _______    _______", curses.A_BOLD)
	typetest.addstr(2, 28, "|         O  |         |       |     |     |\\    |  O  |\\    |  |            |     \\     /  |       |  |", curses.A_BOLD)
	typetest.addstr(3, 28, "|         |  |   ___   |_______|     |     | \\   |  |  | \\   |  |   ___      |      \\   /   |       |  |_______", curses.A_BOLD)
	typetest.addstr(4, 28, "|         |  |  |   |  |       |     |     |  \\  |  |  |  \\  |  |  |   |     |       \\ /    |_______|  |", curses.A_BOLD)
	typetest.addstr(5, 28, "|         |  |      |  |       |     |     |   \\ |  |  |   \\ |  |      |     |        |     |          |", curses.A_BOLD)
	typetest.addstr(6, 28, "|_______  |  |______|  |       |     |     |    \\|  |  |    \\|  |______|     |        |     |          |_______", curses.A_BOLD)
	typetest.addstr(9, 12, target)
	typetest.addstr(12, 50, f"WPM: ")
	typetest.addstr(12, 55, f"{wpm}", curses.A_BOLD)
	typetest.addstr(12, 100, f"Time: ")
	typetest.addstr(12, 106, f"{round(time, 1)}", curses.A_BOLD)

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		typetest.addstr(9, 12+i, char, color)


def load_text():
	with open("Text.txt", "r") as f:
		lines = f.readlines()
		return random.choice(lines).strip()


def wpm_test(typetest):
	target_text = load_text()
	current_text = []
	wpm = 0
	typetest.nodelay(True)

	while True:
		if current_text == []:
			start_time = time.time()
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		typetest.clear()
		display_text(typetest, target_text, current_text, wpm, time_elapsed)
		typetest.refresh()

		if "".join(current_text) == target_text:
			typetest.nodelay(False)
			break

		try:
			key = typetest.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def main(typetest):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

	start_screen(typetest)
	while True:
		wpm_test(typetest)
		typetest.addstr(14, 8, " _______   _______             _______   _______             _______                                   _______      _______             _______")
		typetest.addstr(15, 8, "|         |       |  |\\    |  |         |       |     /\\        |     |       |  |             /\\         |     O  |       |  |\\    |  |          |")
		typetest.addstr(16, 8, "|         |       |  | \\   |  |   ___   |_______|    /  \\       |     |       |  |            /  \\        |     |  |       |  | \\   |  |_______   |")
		typetest.addstr(17, 8, "|         |       |  |  \\  |  |  |   |  |\\          /____\\      |     |       |  |           /____\\       |     |  |       |  |  \\  |          |  |")
		typetest.addstr(18, 8, "|         |       |  |   \\ |  |      |  |  \\       /      \\     |     |       |  |          /      \\      |     |  |       |  |   \\ |          |  |")
		typetest.addstr(19, 8, "|_______  |_______|  |    \\|  |______|  |    \\    /        \\    |     |_______|  |_______  /        \\     |     |  |_______|  |    \\|   _______|  O")
		typetest.addstr(21, 50, "You have completed the test! Press any key to play again!")
		typetest.addstr(22, 70, "Press ESC to exit")
		typetest.refresh()

		key = typetest.getkey()
		if ord(key) == 27:
			break

wrapper(main)