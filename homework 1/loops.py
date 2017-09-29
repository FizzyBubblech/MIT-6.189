#Denis Savenkov
#loops.py

# 1 Using "for" loop set range for num,
# and to find decimal equivalent divide 1.0 on num
for num in range(2, 11):
	print 1.0 / num

# 2 ask user for a number
number = input("Give me a number: ")

# using "while" loop do countdown to zero
if type(number) != int or number < 0:
    print "This is illegal"
else:
    while number >= 0:
        print number
        number -= 1

# 3 ask for base and exp
base = input("Give me a base. ")
exp = input("Give me an exponent. ")

#make "for" loop that counts up the exponents from the base
for i in range(exp):
        print base**i

# 4 ask for a number divisible by 2
number = input("Give me a number that is divisible by 2: ")
# if user gives the number not divisible by 2, ask till he gives correct asnwer
if number%2 != 0:
        while number%2 != 0:
                print "It's not divisible by 2!"
                number = input("Give me a number that is divisible by 2: ")
        if number%2 == 0:
                print "Finally!"

                



    




    
