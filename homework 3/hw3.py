# Name: Denis Savenkov
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######
import math
# **********  Exercise 3.1 ********** 

# Define your function here
def list_intersection(list1, list2):
    #create an empty list to store common elements
    inter_list = []
    #iterate the list and if the element is also in second list
    #and not in inter_list, append the inter_list
    for x in list1:
        if x not in inter_list and x in list2:
            inter_list.append(x)
    return inter_list

print "Test Cases for Exercise 3.1"
print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 3], [3, 3, 3, 2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])
print list_intersection([], [])
print list_intersection([], [1, 3])
print list_intersection([1, 3], [])
print list_intersection([3, 3, 3, 2, 10], [2, 3])

# **********  Exercise 3.2 **********

# Define your function here
def ball_collide(ball1, ball2):
    #calculate the distance between balls, and the sum of their radiuses
    distance = math.sqrt((ball2[0] - ball1[0])**2 + (ball2[1] - ball1[1])**2)
    sumr = ball1[2] + ball2[2]
    #compare the distance and sum of radiuses
    return distance <= sumr
    
print "Test Cases for Exercise 3.2"
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {"6.1":"math","6.2":"literature","6.3":"history",\
              "6.4":"physics","6.5":"chemistry"}

def add_class(class_num, desc):
    #add a class number and the name of the class to dictionary
    my_classes[class_num] = desc

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
    #condition if class listed
    class_listed = False
    for class_num in my_classes.keys():
        #check if class number is in course
        if class_num[0] == course:
            #print out the appropriate class
            print str(class_num) + " - " + my_classes[class_num]
            class_listed = True
    #if class is not listed, print out the response
    if class_listed == False:
        print "No Course " + course + " classes taken"
    
print "Test Cases for Exercise 3.3"
print_classes("6")
print_classes("9")
# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
         'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    #concatenate two lists, key to value by order
    for n in range(0, len(l1)):
        comb_dict[l1[n]] = l2[n]
    return comb_dict

combined_dict = combine_lists(NAMES, AGES)

def people(age):
    #create empty list to store the suitable names
    name_list = []
    #iterate through dict and add names of appropriate age
    for n in combined_dict:
        if combined_dict[n] == age:
            name_list.append(n)
    return name_list

print "Test Cases for Exercise 3.4 (all should be True)"
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
      'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) == ['Bob']
print people(22) == ['Kelly']
print people(23) == []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    #create dictionary for monthes and days of week
    m = {"March":1, "April":2, "May":3, "June":4, "July":5, "August":6, "September":7,\
         "October":8, "November":9, "December":10, "January":11, "February":12}
    week = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",\
            5:"Friday", 6:"Saturday"}
    #create zellers algorithm
    a = m[month]
    if a == 11 or a == 12:
        c = c - 1
    b = day
    c = year % 100
    d = year / 100
    w = (13*a-1) / 5
    x = c / 4
    y = d / 4
    z = w + x + y + b + c - 2*d
    r = z % 7
    if r < 0:
        r += 7
    #return day of week using dictionary
    return week[r]
print "Test Cases for Exercise 3.5"
print zellers("March", 10, 1940) == "Sunday" # This should be True
print zellers("December", 20, 1992) == "Sunday" # True
