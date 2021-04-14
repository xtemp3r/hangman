'''
Version: Alpha_001
created by: xtemp3r

instructions:
 - create list of 50 words
 - pick 1 random word at beginning
 - print " * length of random word
 - let player try until out of lifes or found the word completly
 - if wrong char draw new line in ascii art hangman -1 lifecounter
 - if char right replace " with the correct char
 - create main menu for newgame or exit game
'''

import sys
import os
from colorama import Fore, Back, Style #colored text and background + style to reset setting
import random
from ascii_art import game_visuals #ascii art so its not crammed in here

'''
global variables
'''
banner = '''
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
					  __/ |                      
					 |___/                       
'''
wordlist_file = "wordlist.txt" #location/name of wordlist file
wordlist = [] #actually the list for words in app

'''
setup game stuff
'''
#opens and loads the words from file to list in memory
with open(wordlist_file, "r") as f:
	words = f.read()
	tmp = words.split("\n")
	for w in tmp:
		wordlist.append(w.upper()) #convert all words to UPPERCASE


'''
functions
'''
def playgame(word_to_guess):
	'''
	- refresh lifecounter to 10
	- guessing_word = " * length of word_to_guess
	- 
	'''
	#init fresh game
	print("[DEBUG] word_to_guess: "+word_to_guess)

'''
main menu
'''
while True:
	try:
		print(Fore.BLACK + Back.GREEN + banner) #print banner
		print(Style.RESET_ALL) #reset colorama settings
		usr_input = input("[Menu] Wanna play a game ? [y/n]")
		if usr_input == "y" or usr_input == "Y":
			rando = random.randint(0, 49) #generate fresh int between 0-49 [lists start from 0 so 50-1]
			ret = playgame(wordlist[rando]) #starts the game (function)
			if ret == "GG":
				print("YOU WON AND SURVIVED !!!!")
			elif ret == "FF":
				print("YOU ARE DEAD - GAME OVER")
		else:
			sys.exit("[Menu] Exiting game")
	except Exception as e:
		print("ERROR:")
		sys.exit(e)