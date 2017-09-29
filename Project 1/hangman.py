# Name:Denis Savenkov
# 6.189 Project 1: Hangman template
# hangman.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = get_word()
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### MY CODE ######
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    ####### MY CODE ######
    char_list = []
    for letter in secret_word:
        if letter in letters_guessed:
            char_list.append(letter)
        else:
            char_list.append("-")
    return join(char_list, ' ')

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    ####### MY CODE ######
    while not word_guessed():
        print_hangman_image(mistakes_made)
        print "---------------------------------------"
        print MAX_GUESSES - mistakes_made, "guesses left"
        print print_guessed()
        print "---------------------------------------"
        #get user's input
        letter = lower(raw_input("Enter a letter, or the word 'guess'"\
                               " to try and guess the full word: "))
        #guess the whole word
        if letter == "guess":
            full_word = lower(raw_input("Enter full word: "))
            if full_word == secret_word:
                for char in secret_word:
                    letters_guessed.append(char)
                print "You've guessed the word!", "\n" 
                break
            else:
                mistakes_made += 1
                letter = " "
        #check if it's only one letter
        while len(letter) != 1:
            letter = lower(raw_input("You've entered more than one letter,"\
                                   "please try again: "))
        # check if the letter has already been guessed
        while letter in letters_guessed:
            letter = lower(raw_input("This letter has already been given,"\
                                   "please try again: "))
        #append guessed list
        letters_guessed.append(letter)
        #count mistakes if wrong letter
        if letter not in secret_word:
            mistakes_made += 1
            print "Wrong, sorry.", "\n"
        else:
            print "You've guessed a letter!", "\n"
        #finish game if out of guesses
        if mistakes_made >= MAX_GUESSES:
            print_hangman_image(mistakes_made)
            print "Game Over"
            print "The secret word is:", secret_word
            break

    #finish the game if guessed
    if word_guessed():
        print_hangman_image(mistakes_made)
        print "Congratulations, you won!"
        print "The secret word is:", secret_word


    
