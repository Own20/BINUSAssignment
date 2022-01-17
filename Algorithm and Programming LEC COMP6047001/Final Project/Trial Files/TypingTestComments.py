import curses
#curses module

from curses import wrapper
#initialize curses module, take over terminal to run different commands, after finish restore terminal back

import time
import random

def start_screen(stdscr):
#this function is for accessing the stdscr object to type to the screen
#stdscr = standard output to write stuff to the screen

	stdscr.clear()
	#clears the entire screen

	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	#\n brings the cursor down to the next line / enter

	stdscr.refresh()
	#refresh the screen

	stdscr.getkey()
	#wait for the user to type anything

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}")
	#1 line below the target_text

	for i, char in enumerate(current):
	#enumerate = give/match element from the current_text and index from the target_text list
    #i = index0, char = first element

		correct_char = target[i]
		#compare current_text to target_text if matches with every index in the list

		color = curses.color_pair(1)
		#declare color

		if char != correct_char:
		#if the character doesn't match with the target_text

			color = curses.color_pair(2)
			#it will get color red

		stdscr.addstr(0, i, char, color)
		#i = characters gonna be replaced, so it will overlay on top of target_text
		#i is going up by 1 in every iteration, every character will be incremented by 1 and go directly overtop of target_text

def load_text():
	with open("Text.txt", "r") as f:
	#open file store in f

		lines = f.readlines()
		#open the file in list containing all lines

		return random.choice(lines).strip()
		#randomly choose one of the list in lines
		#strip = remove \n/enter from the lines

def wpm_test(stdscr):
	target_text = load_text()
	#declare load_text function as the target_text
	#print out the target text

	current_text = []
	#things typed by user will inserted to the list

	wpm = 0
	#declare and start the wpm with 0

	start_time = time.time()
	#declares starting time with time module which is a random time number just to be the beginning

	stdscr.nodelay(True)
	#this function will not delay if the user is not typing 

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		#current new time - start time
		#max function is to prevent from getting 0/error
		#if the calculation is less than 1, it will give 1 second

		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
		#(length of current_text divided by (time_elapsed(seconds) divided by 60 to get minutes)) divided by 5 for average characters in a word
		#round is to round the decimal numbers to a flat number

		stdscr.clear()
		#clears the entire screen

		display_text(stdscr, target_text, current_text, wpm)
		#call display_text function

		stdscr.refresh()
		#refresh the screen

		if "".join(current_text) == target_text:
		#join will combine every single character from the list to the "" string/the limiter with a seperator

			stdscr.nodelay(False)
			#show something from the screen and wait the user to type any key before continue

			break
			#break to get out of the while loop

		try:
		#if the user doesn't type anything, try function will make sure the function to not run

			key = stdscr.getkey()
			#wait for the user to type something, so it won't show and close immediately - to keep track what the user type
			#if hit any key, the key will show up
			#this is a block: wait for the user to type

		except:
		#if the function runs and doesn't have a value, it will go to the except function

			continue
			#continue will bring back to the while loop, won't check the rest

		if ord(key) == 27:
		#27 = ASCII for esc key

			break
			#break will get out of the while loop

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
		#backspace can be respresented in many ways depending on the os

			if len(current_text) > 0:
			#if the length of current_text is greater than 0
				current_text.pop()
				#remove the last character/element from the list

		elif len(current_text) < len(target_text):
		#if the length of the current_text is less than the length of the target text

			current_text.append(key)
			#add the keys to the current_text and draw the current_text to the screen, we have all the keys that the user press in the list
			#this will make sure we cannot add more characters unless there is more room


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    #create a pair for foreground and background color
    #parameter: (ID, foreground color, background color)

	start_screen(stdscr)
	#call the start_screen function
	
	while True:
	#to play again as many time
	
		wpm_test(stdscr)
		#call the wpm_test function

		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		#print out the string in the second row

		key = stdscr.getkey()
		#wait for the user to type any key, other than escape key
		
		if ord(key) == 27:
		#if the user hit the escape key

			break
			#it will break/exit

wrapper(main)
#passing the main function to the wrapper function - to call main function while initializing things related to curses module