# Denis Savenkov
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    while pile > 0:
        # print out the number of stones
        print "Player1, there are", pile, "stones left"
        # assign variable for player's answer and set it false initially,
        # so that it would ask him at least once 
        player1 = 0
        while not(player1 >= 1 and player1 <= max_stones and player1 <= pile):
            player1 = input("Player1: How many stones will you take? ")
            # legal answer? 
            if not(player1 >= 1 and player1 <= max_stones and player1 <= pile):
                print "This is invalid input."
        # subtract from the pile the amount player answered
        pile -= player1
        if pile == 0:
            print "Congrats Player1, you won!"
            break
        # same for player 2
        print "Player2, there are", pile, "stones left"
        player2 = 0
        while not(player2 >= 1 and player2 <= max_stones and player2 <= pile):
            player2 = input("Player2: How many stones will you take? ")
            if not(player2 >= 1 and player2 <= max_stones and player2 <= pile):
                print "This is invalid input."
        pile -= player2
        if pile == 0:
            print "Congrats Player2, you won!"
            break
    print "Game over"

# test cases
play_nims(100, 5)
play_nims(100, 3)
play_nims(20, 5)
