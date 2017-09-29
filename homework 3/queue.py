#Name: Denis Savenkov
#queue.py

#class for Queue
class Queue:
    # init method
    def __init__(self, line=[]):
        self.line = line
    #insert new element method
    def insert(self, element):
        self.line.append(element)
    #remove element method
    def remove(self):
        if self.line == []:
            print "The queue is empty"
        else:
            a = self.line[0]
            del self.line[0]
            return a
            
