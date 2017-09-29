# MIT 6.189
# Project 1
# Author: Denis Savenkov
# File: questions sol.py

def all_less_6(a_list):
    for val in a_list:
        if val >= 6:
            return False
    return True

list1 = [1, 5, 3, 4]
list2 = [5, 3, 7, 5]
print all_less_6(list1)
print all_less_6(list2)

def one_less_6(a_list):
    for val in a_list:
        if val < 6:
            return True
    return False

list3 = [7, 8, 7, 9]
list4 = [7, 2, 5, 8]
print one_less_6(list3)
print one_less_6(list4)
