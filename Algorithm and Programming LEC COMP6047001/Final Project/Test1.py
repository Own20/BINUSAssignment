import curses
from curses import wrapper
from json import load
import time
import random

def start_screen(stdscr):
	stdscr.clear()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

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
	current_text = []
	wpm = 0
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

		display_text(stdscr, target_text, current_text, wpm)
        #call display_text function

		stdscr.refresh()

		if "".join(current_text) == target_text:
		#join will combine every single character from the list to the "" string/the limiter with a seperator
			stdscr.nodelay(False)
			#show something from the screen and wait the user to type any key before continue
			break
			#to get out of the while loop

		try:
		#if the user doesn't type anything, try function will make sure the function to not run
			key = stdscr.getkey()
			#this is a block: wait for the user to type
		except:
			#if the function runs and doesn't have a value, it will go to the except function
			continue
			#continue will bring back to the while loop, won't check the rest

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", "\b", "\x7f"):
			if len(current_text) > 0:
				current_text.pop()

		elif len(current_text) < len(target_text):
		#if the length of the current_text is less than the length of the target text

			current_text.append(key)
			#this will make sure we cannot add more characters unless there is more room

def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(stdscr)

	while True:
	#to play again as many time
		wpm_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		#print out the string in the second row
		key = stdscr.getkey()
		#wait for the user to type any key, other than escape key
		
		if ord(key) == 27:
		#if the user hit the escape key
			break
			#it will break/exit
	
wrapper(main)