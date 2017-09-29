# Name: Denis Savenkov
# hw2.py

import math
import random

##### Template for Homework 2, exercises 2.0 - 2.5  ######

print "**********  Exercise 2.0 **********" 

#two functions: one - to print out x + 1, other - to return x + 1
def f1(x):
    print x + 1

def f2(x):
    return x + 1

print "**********  Exercise 2.1 **********" 
#Create a truth table:

###################################
# Player 1 # Player 2 # Result
# # # # # # # # # # # # # # # # # #
# Rock     # Rock     #  Tie
# Rock     # Scissors #  Player 1
# Rock     # Paper    #  Player 2
# Scissors # Scissors #  Tie
# Scissors # Paper    #  Player 1
# Scissors # Rock     #  Player 2
# Paper    # Paper    #  Tie
# Paper    # Rock     #  Player 1
# Paper    # Scissors #  Player 2
###################################

#create variables for rock,paper,scissor and for results:
r = "rock"
p = "paper"
s = "scissors"
t = "Tie."
p1 = "Player 1 wins."
p2 = "Player 2 wins."

#create conditions for output
def winner(player1, player2):
    if (player1 == r and player2 == r):
        return t
    elif (player1 == r and player2 == s):
        return p1
    elif (player1 == r and player2 == p):
        return p2
    elif (player1 == s and player2 == s):
        return t
    elif (player1 == s and player2 == r):
        return p2
    elif (player1 == s and player2 == p):
        return p1
    elif (player1 == p and player2 == p):
        return t
    elif (player1 == p and player2 == r):
        return p1
    elif (player1 == p and player2 == s):
        return p2
#if not valid input - print the message
    else:
        return "This is not a valid object selection"

# Test Cases for Exercise 2.1
print "winner test cases"
print winner("rock", "rock") #Should be Tie
print winner("rock", "paper") #Should be Player 2
print winner("rock", "scissors") #Should be Player 1

print "********** Exercise 2.2 **********" 

# define a function that returns True if m is divisible by n, False otherwise
def is_divisible(m, n):
    if m > 0 and n > 0:
        return m%n == 0
    else:
        return "Error"
    
# Test cases for is_divisible
print "is_divisible tests"
print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return? error

# Define not_equal function, that returns True if a not equal b, False otherwise
def not_equal(a, b):
    return a != b

# Test cases for not_equal
print "not_equal function tests"
print not_equal(1, 1) #False
print not_equal(1, 2) #True
print not_equal(-1, 2) #True

print "********** Exercise 2.3 **********" 

## 1 - multadd function
def multadd(a, b, c):
    return a * b + c
# Test cases for multadd
print "multadd function tests"
print multadd(1, 2, 3) #should be 5
print multadd(-1, 2, 3) #should be 1
print multadd(0, 2, 3) #should be 3

## 2 - Equations
#angle_test
multadd(1, math.sin(math.pi/4), math.cos(math.pi/4) / 2)

#ceiling_test
multadd(2, math.log(12,7), math.ceil(276/19))

# Test Cases
angle_test = multadd(1, math.sin(math.pi/4), math.cos(math.pi/4) / 2)
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multadd(2, math.log(12,7), math.ceil(276/19))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
def yikes(x):
    return multadd(x, math.e**(-x),(1 - math.e**(-x))**0.5)

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

print "********** Exercise 2.4 **********"

## 1 - rand_divis_3 function
def rand_divis_3():
    x = random.randint(1, 100)
    print x
    return x%3 == 0
    
# Test Cases
print "test rand_divis_3()", rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(sides, num_dice):
    while num_dice > 0:
        print random.randint(1, sides)
        num_dice -= 1
    return "That's all!"

# Test Cases
print "roll the dice!", roll_dice(5, 3)   
print "and then?", roll_dice(4, 2)
print "and then??", roll_dice(3, 6)                          

print "********** Exercise 2.5 **********"

# function for finding roots of quadratic equation
def roots(a, b, c):
    if (b**2 - 4*a*c) > 0:
        x = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        y = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
        return x, y
    elif (b**2 - 4*a*c) < 0:          #can't take sqrt of a negative number
        return "No real roots"
    elif (b**2 - 4*a*c) == 0:
        x = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        return x
    else:
        return "error"

# Test Cases
print "Test Cases for Roots Functions"
print roots(1, 2, 3)
print roots(0, 0, 4)
print roots(-4, 3, 2)
