# Name: Denis Savenkov
# game_of_life.py

from graphics import *
import random

## Written by Sarina Canelake & Kelly Casteel, August 2010
## Revised January 2011

############################################################
# GLOBAL VARIABLES
############################################################
    
BLOCK_SIZE = 40
BLOCK_OUTLINE_WIDTH = 2
BOARD_WIDTH = 12
BOARD_HEIGHT = 12

neighbor_test_blocklist = [(0,0), (1,1)]
toad_blocklist = [(4,4), (3,5), (3,6), (5,7), (6,5), (6,6)]
beacon_blocklist = [(2,3), (2,4), (3,3), (3,4), (4,5), (4,6), (5,5), (5,6)]
glider_blocklist = [(1,2), (2,3), (3,1), (3,2), (3,3)]
pulsar_blocklist = [(2,4), (2,5), (2,6), (4,2), (4,7), (5,2), (5,7),
                    (6,2), (6,7), (7,4), (7,5), (7,6), ]
# for diehard, make board at least 25x25, might need to change block size
diehard_blocklist = [(5,7), (6,7), (6,8), (10,8), (11,8), (12,8), (11,6)]

############################################################
# TEST CODE (don't worry about understanding this section)
############################################################

def test_neighbors(board):
    '''
    Code to test the board.get_block_neighbor function
    '''
    for block in board.block_list.values():
        neighbors = board.get_block_neighbors(block)
        ncoords = [neighbor.get_coords() for neighbor in neighbors]
        if block.get_coords() == (0,0):
            zeroneighs = [(0,1), (1,1), (1,0)]
            for n in ncoords:
                if n not in zeroneighs:
                    print "Testing block at (0,0)"
                    print "Got", ncoords
                    print "Expected", zeroneighs
                    return False

            for neighbor in neighbors:
                if neighbor.get_coords() == (1, 1):
                    if neighbor.is_live() == False:
                        print "Testing block at (0, 0)..."
                        print "My neighbor at (1, 1) should be live; it is not."
                        print "Did you return my actual neighbors, or create new copies of them?"
                        print "FAIL: get_block_neighbors() should NOT return new Blocks!"
                        return False

        elif block.get_coords() == (1,1):
            oneneighs = [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1),(2,2)]
            for n in ncoords:
                if n not in oneneighs:
                    print "Testing block at (1,1)"
                    print "Got", ncoords
                    print "Expected", oneneighs
                    return False
            for n in oneneighs:
                if n not in ncoords:
                    print "Testing block at (1,1)"
                    print "Got", ncoords
                    print "Expected", oneneighs
                    return False
    print "Passed neighbor test"
    return True


############################################################
# BLOCK CLASS (Read through and understand this part!)
############################################################

class Block(Rectangle):
    ''' Block class:
        Implement a block for a tetris piece
        Attributes: x - type: int
                    y - type: int
        specify the position on the board
        in terms of the square grid
    '''

    def __init__(self, pos, color="red"):
        '''
        pos: a Point object specifing the (x, y) square of the Block (NOT in pixels!)
        color: a string specifing the color of the block (eg 'blue' or 'purple')
        '''
        self.x = pos.x
        self.y = pos.y
        
        p1 = Point(pos.x*BLOCK_SIZE,
                   pos.y*BLOCK_SIZE)
        p2 = Point(p1.x + BLOCK_SIZE, p1.y + BLOCK_SIZE)

        Rectangle.__init__(self, p1, p2)
        self.setWidth(BLOCK_OUTLINE_WIDTH)
        self.setFill(color)
        self.status = 'dead'
        self.new_status = 'None'
        
    def get_coords(self):
        return (self.x, self.y)

    def set_live(self, canvas):
        '''
        Sets the block status to 'live' and draws it on the grid.
        Be sure to do this on the canvas!
        '''
        if self.status=='dead':
          self.status = 'live'
          self.draw(canvas)

    def set_dead(self):
        '''
        Sets the block status to 'dead' and undraws it from the grid.
        '''
        if self.status=='live':
          self.status = 'dead'
          self.undraw()

    def is_live(self):
        '''
        Returns True if the block is currently 'live'. Returns False otherwise.
        '''
        if self.status == 'live':
            return True
        return False

    def reset_status(self, canvas):
        '''
        Sets the new_status to be the current status
        '''
        if self.new_status=='dead':
            self.set_dead()
        elif self.new_status=='live':
            self.set_live(canvas)
        

###########################################################
# BOARD CLASS (Read through and understand this part!)
# Print out and turn in this section.
# Name: Denis Savenkov
# Recitation:
###########################################################

class Board(object):
    ''' Board class: it represents the Game of Life board

        Attributes: width - type:int - width of the board in squares
                    height - type:int - height of the board in squares
                    canvas - type:CanvasFrame - where the blocks will be drawn
                    block_list - type:Dictionary - stores the blocks for a given position
    '''
    
    def __init__(self, win, width, height):
        self.width = width
        self.height = height
        self.win = win
        # self.delay is the number of ms between each simulation. Change to be
        # shorter or longer if you wish!
        self.delay = 1000

        # create a canvas to draw the blocks on
        self.canvas = CanvasFrame(win, self.width * BLOCK_SIZE,
                                       self.height * BLOCK_SIZE)
        self.canvas.setBackground('white')

        # initialize grid lines
        for x in range(1, self.width):
            self.draw_gridline(Point(x, 0), Point(x, self.height))

        for y in range(1, self.height):
            self.draw_gridline(Point(0, y), Point(self.width, y))

        # For each square on the board, we need to initialize
        # a block and store that block in a data structure. A
        # dictionary (self.block_list) that has key:value pairs of
        # (x,y):Block will be useful here.
        self.block_list = {}

        ####### MY CODE ######
        
        #iterate through columns
        for x in range(0, self.width):
            #iterate through rows
            for y in range(0, self.height):
                #add the block to dictionary
                self.block_list[(x,y)] = Block(Point(x,y))

    def draw_gridline(self, startp, endp):
        ''' Parameters: startp - a Point of where to start the gridline
                        endp - a Point of where to end the gridline
            Draws two straight 1 pixel lines next to each other, to create
            a nice looking grid on the canvas.
        '''
        line = Line(Point(startp.x*BLOCK_SIZE, startp.y*BLOCK_SIZE), \
                    Point(endp.x*BLOCK_SIZE, endp.y*BLOCK_SIZE))
        line.draw(self.canvas)
        
        line = Line(Point(startp.x*BLOCK_SIZE-1, startp.y*BLOCK_SIZE-1), \
                    Point(endp.x*BLOCK_SIZE-1, endp.y*BLOCK_SIZE-1))
        line.draw(self.canvas)


    def random_seed(self, percentage):
        ''' Parameters: percentage - a number between 0 and 1 representing the
                                     percentage of the board to be filled with
                                     blocks
            This method activates the specified percentage of blocks randomly.
        '''
        for block in self.block_list.values():
            if random.random() < percentage:
                block.set_live(self.canvas)

    def seed(self, block_coords):
        '''
        Seeds the board with a certain configuration.
        Takes in a list of (x, y) tuples representing block coordinates,
        and activates the blocks corresponding to those coordinates.
        '''

        #### MY CODE #####
        
        for pos in block_coords:
            self.block_list[pos].set_live(self.canvas)

    def get_block_neighbors(self, block):
        '''
        Given a Block object, returns a list of neighboring blocks.
        Should not return itself in the list.
        '''
        #### MY CODE #####
        
        #### Think about edge conditions!
        b, x, y = self.block_list, block.x, block.y

        if x == 0:
            if y == 0:
                return [b[x+1,y], b[x+1,y+1], b[x,y+1]]
            elif y == self.height - 1:
                return [b[x,y-1], b[x+1,y-1], b[x+1,y]]
            else:
                return [b[x,y+1], b[x+1,y+1], b[x+1,y],\
                        b[x+1,y-1], b[x,y-1]]

        elif x == self.width - 1:
            if y == 0:
                return [b[x-1,y+1], b[x,y+1], b[x-1,y]]
            elif y == self.height-1:
                return [b[x,y-1], b[x-1,y-1], b[x-1,y]]
            else:
                return [b[x-1,y+1] ,b[x,y+1], b[x,y-1],\
                        b[x-1,y-1], b[x-1,y]]

        else:
            if y == 0:
                return [b[x-1,y+1], b[x,y+1], b[x+1,y+1],\
                        b[x+1,y], b[x-1,y]]
            elif y == self.width - 1:
                return [b[x+1,y], b[x+1,y-1], b[x,y-1],\
                        b[x-1,y-1], b[x-1,y]]
            else:
                return [b[x-1,y+1], b[x,y+1], b[x+1,y+1],\
                        b[x+1,y], b[x+1,y-1], b[x,y-1],\
                        b[x-1,y-1], b[x-1,y]]
            
    def simulate(self):
        '''
        Executes one turn of Conways Game of Life using the rules
        listed in the handout. Best approached in a two-step strategy:
        
        1. Calculate the new_status of each block by looking at the
           status of its neighbors.

        2. Set blocks to 'live' if their new_status is 'live' and their
           status is 'dead'. Similarly, set blocks to 'dead' if their
           new_status is 'dead' and their status is 'live'. Then, remember
           to call reset_status(self.canvas) on each block.
        '''

        #### MY CODE #####
        
        #checks neighbors for live cells and returns the number
        def live_neighbors(block):
            n = 0
            for block in self.get_block_neighbors(block):
                if block.is_live():
                    n += 1
            return n

        #sets new status for blocks
        def new_status():
            for block in self.block_list.values():
                #if block is "live"
                if block.is_live():
                    #has less than 2 or more than 3 live neighbors,
                    #set new status to "dead", else "live"
                    if live_neighbors(block) < 2 or live_neighbors(block) > 3:
                        block.new_status = "dead"
                    else:
                        block.new_status = "live"
                #if block is "dead" and has 3 "live" neighbors,
                #set new_status to "live", else "dead"
                elif live_neighbors(block) == 3:
                    block.new_status = "live"
                else:
                    block.new_status = "dead"

        #resets status of blocks, according to new_status
        def reset():
            new_status()
            for block in self.block_list.values():
                block.reset_status(self.canvas)

        reset()
        
    def animate(self):
        '''
        Animates the Game of Life, calling "simulate"
        once every second
        '''
        self.simulate()
        self.win.after(self.delay, self.animate)



################################################################
# RUNNING THE SIMULATION
################################################################

if __name__ == '__main__':    
    # Initalize board
    win = Window("Conway's Game of Life")
    board = Board(win, BOARD_WIDTH, BOARD_HEIGHT)

    ## PART 1: Make sure that the board __init__ method works    
    #board.random_seed(.15)

    ## PART 2: Make sure board.seed works. Comment random_seed above and uncomment
    ##  one of the seed methods below
    #board.seed(toad_blocklist)

    ## PART 3: Test that neighbors work by commenting the above and uncommenting
    ## the following two lines:
    #board.seed(neighbor_test_blocklist)
    #test_neighbors(board)


    ## PART 4: Test that simulate() works by uncommenting the next two lines:
    board.seed(beacon_blocklist)
    #win.after(2000, board.simulate)

    ## PART 5: Try animating! Comment out win.after(2000, board.simulate) above, and
    ## uncomment win.after below.
    win.after(2000, board.animate)

    ## Yay, you're done! Try seeding with different blocklists (a few are provided at the top of this file!)
    
    win.mainloop()
                
