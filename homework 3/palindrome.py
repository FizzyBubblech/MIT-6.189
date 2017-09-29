#Denis Savenkov
#palindrome.py

#checks if palindrome
def is_palindrome(string):
    #cases if an empty string or not a string
    if type(string) != str:
        return False
    if len(string) == 0:
        return False
    #lowercase and remove spaces
    string = string.lower()
    string = string.replace(" ","")
    #create a reverse string
    reverse = ""
    i = len(string) - 1
    while i >= 0:
        substr = string[i]
        reverse += substr
        i -= 1
    #compare it to a string
    return string == reverse

#test cases
tests = [True, 12, "", "a", "as", "ana", "Anna", "parameter",\
        "able was i ere i saw elba", "able was i ere i saw elba"]
for t in tests:
    print t, "-->", is_palindrome(t)

#recursion alternative
def is_palindrome_rec(s):
    if type(s) != str:
        return False
    # base case before the or; recursive case after the or
    if len(s) <= 1 or s[0] == s[-1] and is_palindrome(s[1:-1]):
        return True
    return False

#test cases
print "\trecursion test"
strs = [False, 17, "", "a", "as", "ask", "ewe", "emma",\
        "dromedary", "racecar"]
for s in strs:
    print("%s --> %s" % (s, is_palindrome_rec(s)))
