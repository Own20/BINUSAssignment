import curses
from curses import wrapper

def start_screen(stdscr):
#this function is for accessing the stdscr object to type to the screen

	stdscr.clear()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
    #\n brings the cursor down to the next line / enter

	stdscr.refresh()
	stdscr.getkey()
    #wait for the user to type anything

def wpm_test(stdscr):
	target_text = "Hello world this is some test text for this app!"
	#print out the target text

	current_text = []
	#things typed by user will inserted to the list

	while True:
		stdscr.clear()
        #clear the screen every single time the while loop runs
		stdscr.addstr(target_text)
        #add target text to the screen

		for char in current_text:
		#loop every single key and place the character to the screen

			stdscr.addstr(char, curses.color_pair(1))
			#char = whatever the user typed, and the color that wanted

		stdscr.refresh()
        #refresh the screen

		key = stdscr.getkey()

		if ord(key) == 27:
		#27 = ASCII for esc key
			break
			#break will get out of the while loop

		if key in ("KEY_BACKSPACE", "\b", "\x7f"):
		#backspace can be respresented in many ways depending on the os
			if len(current_text) > 0:
				current_text.pop()
				#remove the last character/element from the list
		else:
			current_text.append(key)
			#add the keys to the current_text and draw the current_text to the screen, we have all the keys that the user press in the list

def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(stdscr)
    #call the start_screen function
	wpm_test(stdscr)
    #call the wpm_test function
	
wrapper(main)