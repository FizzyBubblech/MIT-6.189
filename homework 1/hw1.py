# Savenkov Denis
# hw1.py

##### Template for Homework 1, exercises 1.2-1.5 ######

print "********** Exercise 1.2 **********"

# Do your work for Exercise 1.2 here

# print tic-tac-toe board using print command

print "  |  |  "
print "--------"
print "  |  |  "
print "--------"
print "  |  |  "


print "********** Exercise 1.3 **********"

# assign values to variables

a = "  |  |  "
b = "--------"

# print tic-tac-toe board using variables

print a
print b
print a
print b
print a

print "********** Exercise 1.4 **********"
print "********* Part II *************"

# assign transcribed equations to variables

a = (3 * 5) / (2 + 3)
b = (7 + 9)**(0.5 * 2)
c = (4 - 7)**3
d = (-19 + 100)**0.25
e = 6 % 4

# print the variables

print a, b, c, d, e

print "********* Part III *************"

# assign two similar looking equations to variables

x = (3 * 4) - 2
y = 3 * (4 - 2)

# print the variables

print x, y

print "********** Exercise 1.5 **********"

# collect name from user

first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")

# collect date of birth from user

print "Enter your date of birth:"
month = raw_input("Month? ")
day = raw_input("Day? ")
year = raw_input("Year? ")

#print the result

print first_name, last_name, "was born on", month, day+",", year+"."
