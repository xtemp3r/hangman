#Hangman
#Version: Beta
#created by: xtemp3r
import sys
from os import system
import random
from ascii_art import game_visuals #ascii art so its not crammed in here

'''
global variables
'''
banner = '''
                                                                            
_|    _|                                                                    
_|    _|    _|_|_|  _|_|_|      _|_|_|  _|_|_|  _|_|      _|_|_|  _|_|_|    
_|_|_|_|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|  
_|    _|  _|    _|  _|    _|  _|    _|  _|    _|    _|  _|    _|  _|    _|  
_|    _|    _|_|_|  _|    _|    _|_|_|  _|    _|    _|    _|_|_|  _|    _|  
                                    _|                                      
                                _|_|                                        

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
	#init fresh game
	masked_word = str("*"*len(word_to_guess))
	life_counter = 10
	guessed = []
	tmp_msg = "Good luck !" #empty for first run
	while life_counter != 0:
		system("clear") #clear the screen
		print(banner) #print banner
		print(game_visuals[life_counter])
		#print("[DEBUG]: Word to guess: "+word_to_guess)
		print("[INFO]: " + tmp_msg)
		print("[LIFE]: " + str(life_counter))
		print(masked_word)
		usr_guess = input("Input char: ").upper() #convert to uppercase
		#eval input
		if usr_guess in guessed:
			tmp_msg = ("You already tried this")
		elif usr_guess == word_to_guess:
			#direct win !
			print("The word is: {} !!!".format(word_to_guess))
			return "GG"
		elif len(usr_guess) != 1:
			tmp_msg = ("Length not 1")
		else:
			guessed.append(usr_guess)
			splitter = list(masked_word)
			for index, char in enumerate(word_to_guess):
				if char == usr_guess:
					#got a guess
					splitter[index] = usr_guess
			if "".join(splitter) == masked_word:
				life_counter = life_counter - 1 #lose a life nothing changed
			else:
				masked_word = "".join(splitter)
			if masked_word == word_to_guess:
				print("The word is: {} !!!".format(word_to_guess))
				return "GG" #game is won
	return "FF"

'''
main menu
'''
while True:
	try:
		system("clear") #clear the screen
		print(banner) #print banner
		usr_input = input("[Menu] Wanna play a game ? [y/n]")
		if usr_input == "y" or usr_input == "Y":
			rando = random.randint(0, 49) #generate fresh int between 0-49 [lists start from 0 so 50-1]
			ret = playgame(wordlist[rando]) #starts the game (function)
			if ret == "GG":
				print("YOU WON AND SURVIVED !!!!")
				input("Press enter to continue")
			elif ret == "FF":
				print("YOU ARE DEAD - GAME OVER")
				input("Press enter to continue")
		else:
			sys.exit("[Menu] Exiting game")
	except Exception as e:
		print("ERROR:")
		sys.exit(e)