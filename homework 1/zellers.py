# Denis Savenkov
# zellers.py

# collect date of birth from user
print "Enter your date of birth:"
month = input("Month as a number between 1 and 12, starting from March? ")
day = input("Day? ")
year = input("Year? ")

#create zellers algorithm
a = month
if a == 11 or a == 12:
    c = c - 1
b = day
c = year % 100
d = year / 100
w = (13*a - 1) / 5
x = c / 4
y = d / 4
z = w + x + y + b + c - 2*d
r = z % 7
if r < 0:
    r += 7

#print out the day
if r == 0:
    print "Sunday"
if r == 1:
    print "Monday"
if r == 2:
    print "Tuesday"
if r == 3:
    print "Wednesday"
if r == 4:
    print "Thursday"
if r == 5:
    print "Friday"
if r == 6:
    print "Saturday"
    
