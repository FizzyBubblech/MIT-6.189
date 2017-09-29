#Denis Savenkov
#stacks.py

#Stack class
class Stack:
    #initialize
    def __init__(self, items=[]):
        self.items = items
    #add element
    def push(self, element):
        self.items.append(element)
    #remove element
    def pop(self):
        if self.items == []:
            print "The stack is empty"
        else:
            e = self.items[-1]
            del self.items[-1]
            return e

