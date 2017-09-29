# Denis Savenkov
# strings_and_lists.py

import string
print "**********  Exercise 2.7 **********"

# takes a list of numbers and returns sum of all numbers
def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num
    return total

# Test cases
print "\tTest 2.7 sum_all"
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])

# returns cumulative sum
def cumulative_sum(number_list):
    # number_list is a list of numbers
    total = 0
    cum_list=[] #create an empty list
    for num in number_list:
        total += num
        cum_list.append(total) #add total to the list

    return cum_list

# Test Cases
print "\tTest ex 2.7 cumulative_sum"
print "cumulative_sum of [4,3,6] is:", cumulative_sum([4,3,6])
print "cumulative_sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4])

print "**********  Exercise 2.8 **********"

# asks users for classes and grades and prints out GPA card
def report_card():
    #Get number of classes taken
    n = input("How many classes did you take? ")
    #Condition for zero or negative answer
    if n <= 0:
        print "REPORT CARD: "
        print "You have not taken any course yet. "
    #create empty lists for classes and grades 
    classes = []
    grades = []
    #loop for answers for number of classes, and create lists from answers
    for c in range(n):
        class_n = raw_input("What was the name of this class? ")
        classes.append(class_n)
        grade = input("What was your grade? ")
        grades.append(grade)
    # Print out report
    print "REPORT CARD: "
    for i in range(n):
        print classes[i],"-", grades[i]
    print "Overall GPA -", sum_all(grades)*1.0/n
            
# Test Cases
print "\tTest ex 2.8"
report_card()
# In comments, show the output of one run of your function.
#How many classes did you take? 2
#What was the name of this class? p
#What was your grade? 1
#What was the name of this class? v
#What was your grade? 2
#REPORT CARD: 
#p - 1
#v - 2
#Overall GPA - 1.5

print "**********  Exercise 2.9 **********"

# Write any helper functions you need here.
VOWELS = ['a', 'e', 'i', 'o', 'u']

#takes a word and convers to pig_latin
def pig_latin(word):
    #condition for input other than string
    if type(word) != str or len(word) == 0:
        return "incorrect input"
    #convert to lowercase
    word_lower = word.lower()
    if word_lower[0] in VOWELS:
        return word_lower + "hay"
    else:
        return word_lower[1:] + word_lower[0] + "ay"

# Test Cases
print "\tTest ex 2.9"
print "'word' in pig latin is", pig_latin("word")
print "'WORD' in pig latin is", pig_latin("WORD")
print "'image' in pig latin is", pig_latin("image")
print "'IMAGE' in pig latin is", pig_latin("IMAGE")
print "'111111' in pig latin is", pig_latin(1111)
print "'' in pig latin is", pig_latin("")

print "**********  Exercise 2.10 **********"
# Test Cases
#1
#prints out a list of cubes from 1 to 10
print "[x**3 for x in range(1, 11)] is", [x**3 for x in range(1, 11)]
#2
#prints out result of a coin flip
print [i + j for i in 'ht' for j in 'ht']
#3
#takes in a string and returns all the vowels in a string
def vowels():
    word = raw_input("Give me a word. ")
    print [x for x in word if x in 'aeiou' or x in 'AEIOU']
vowels()
#4
[x + y for x in [10, 20, 30] for y in [1, 2, 3]]

def sum1():
    for x in [10 ,20, 30]:
        #now add to y
        for y in [1, 2, 3]:
            y += x
            print y

print sum1()
