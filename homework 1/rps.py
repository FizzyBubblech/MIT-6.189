# Savenkov Denis
# rps.py

#create variables for rock,paper,scissor and for results:
r = "rock"
p = "paper"
s = "scissors"
t = "Tie."
p1 = "Player 1 wins."
p2 = "Player 2 wins."

#get figure from players
player1 = raw_input("Player 1? ")
player2 = raw_input("Player 2? ")

#create conditions for output
if (player1 == r and player2 == r):
    print t
elif (player1 == r and player2 == s):
    print p1
elif (player1 == r and player2 == p):
    print p2
elif (player1 == s and player2 == s):
    print t
elif (player1 == s and player2 == r):
    print p2
elif (player1 == s and player2 == p):
    print p1
elif (player1 == p and player2 == p):
    print t
elif (player1 == p and player2 == r):
    print p1
elif (player1 == p and player2 == s):
    print p2
#if not valid input print out a message
else:
    print "This is not a valid object selection"

    
