#Denis Savenkov
#cipher.py

import string

#Ask for a phrase to encode and the shift value
phrase = raw_input("Enter sentence to encrypt: ")
shift = input("Enter shift value: ")

#create an empty string
encoded_phrase = ""

#traverse through letters
for letter in phrase:
    #get ascii index
    code = ord(letter)
    #shift it
    if code in range(65, 91):
        code = code + shift
        code = code % 91
        if code < 65:
            code = code + 65
    elif code in range(97, 123):
        code = code + shift
        code = code % 123
        if code < 97:
            code = code + 97
    #get a letter again and add it to encoded phrase
    letter = chr(code)
    encoded_phrase = encoded_phrase+letter

#print out result
print "The encoded phrase is: " + encoded_phrase
