#Denis Savenkov
#Pig_latin.py

import string

VOWELS = ['a', 'e', 'i', 'o', 'u']
PUNCT = [",", ".", "!", "?", ":", ";"]

#function to convert word
def pig_latin_word(word):
    #convert to lowercase
    word_lower = word.lower()
    if word_lower[0] in VOWELS:
        return word_lower + "hay"
    else:
        return word_lower[1:] + word_lower[0] + "ay"

#function to convert phrase
def pig_latin_phrase(phrase):
    #split the phrase in a list
    word_list = phrase.split()
    #empty string to concatenate word to
    pig_latin_phrase = ""
    for word in word_list:
        w = pig_latin_word(word)
        pig_latin_phrase += w+" "
    return pig_latin_phrase

#main function to ask for a phrase and convert it
def main():
    phrase = raw_input("Enter a phrase, without punctuation: ")
    while phrase != "Quit":
        print pig_latin_phrase(phrase)
        phrase = raw_input("Enter a phrase, without punctuation: ")

main()
