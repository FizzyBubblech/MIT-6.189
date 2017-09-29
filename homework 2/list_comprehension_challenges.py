#Denis Savenkov
#list_comprehension_challenges.py

# ex 1
#takes in a list of different type elements and returns only ints
def return_int(list):
    return [x for x in list if isinstance(x, int)]

list=["a", 2.13, 2, 4, "b"]
print return_int(list)

# ex 2
# solves the equation y = x2 +1
print [[x, y] for x in range(-5, 5) for y in range(0, 10) if y == (x**2) + 1]
 
# ex 3
#finds the integer solutions [x, y] for a circle of radius 5
print [[x, y] for x in range(-5, 5) for y in range(0, 10) if y**2 + x**2 == 5**2]
