# Name: Denis Savenkov
# tetris.py

from graphics import *
import random

############################################################
# BLOCK CLASS
############################################################

class Block(Rectangle):
    ''' Block class:
        Implement a block for a tetris piece
        Attributes: x - type: int
                    y - type: int
        specify the position on the tetris board
        in terms of the square grid
    '''

    BLOCK_SIZE = 30
    OUTLINE_WIDTH = 3

    def __init__(self, pos, color):
        self.x = pos.x
        self.y = pos.y
        
        p1 = Point(pos.x*Block.BLOCK_SIZE + Block.OUTLINE_WIDTH,
                   pos.y*Block.BLOCK_SIZE + Block.OUTLINE_WIDTH)
        p2 = Point(p1.x + Block.BLOCK_SIZE, p1.y + Block.BLOCK_SIZE)

        Rectangle.__init__(self, p1, p2)
        self.setWidth(Block.OUTLINE_WIDTH)
        self.setFill(color)

    def can_move(self, board, dx, dy):
        ''' Parameters: dx - type: int
                        dy - type: int

            Return value: type: bool
                        
            checks if the block can move dx squares in the x direction
            and dy squares in the y direction
            Returns True if it can, and False otherwise
            HINT: use the can_move method on the Board object
        '''
        
        ####### MY CODE ######
        
        x = self.x + dx
        y = self.y + dy
        return board.can_move(x, y)
    
    def move(self, dx, dy):
        ''' Parameters: dx - type: int
                        dy - type: int
                        
            moves the block dx squares in the x direction
            and dy squares in the y direction
        '''

        self.x += dx
        self.y += dy

        Rectangle.move(self, dx*Block.BLOCK_SIZE, dy*Block.BLOCK_SIZE)

############################################################
# SHAPE CLASS
############################################################

class Shape():
    ''' Shape class:
        Base class for all the tetris shapes
        Attributes: blocks - type: list - the list of blocks making up the shape
                    rotation_dir - type: int - the current rotation direction of the shape
                    shift_rotation_dir - type: Boolean - whether or not the shape rotates
    '''

    def __init__(self, coords, color):
        self.blocks = []
        self.rotation_dir = 1
        ### A boolean to indicate if a shape shifts rotation direction or not.
        ### Defaults to false since only 3 shapes shift rotation directions (I, S and Z)
        self.shift_rotation_dir = False
        
        for pos in coords:
            self.blocks.append(Block(pos, color))

    def get_blocks(self):
        '''returns the list of blocks
        '''
        
        ####### MY CODE ######
        
        return self.blocks

    def draw(self, win):
        ''' Parameter: win - type: CanvasFrame

            Draws the shape:
            i.e. draws each block
        ''' 
        for block in self.blocks:
            block.draw(win)

    ####### MY CODE ######
    # optional ex
    def undraw(self):
        ''' Parameter: win - type: CanvasFrame

            Undraws the shape:
            i.e. undraws each block
        ''' 
        for block in self.blocks:
            block.undraw()

    def move(self, dx, dy):
        ''' Parameters: dx - type: int
                        dy - type: int

            moves the shape dx squares in the x direction
            and dy squares in the y direction, i.e.
            moves each of the blocks
        '''
        for block in self.blocks:
            block.move(dx, dy)

    def can_move(self, board, dx, dy):
        ''' Parameters: dx - type: int
                        dy - type: int

            Return value: type: bool
                        
            checks if the shape can move dx squares in the x direction
            and dy squares in the y direction, i.e.
            check if each of the blocks can move
            Returns True if all of them can, and False otherwise
           
        '''
        
        ####### MY CODE ######
        
        for block in self.blocks:
            if not block.can_move(board, dx, dy):
                return False
        return True
            
    
    def get_rotation_dir(self):
        ''' Return value: type: int
        
            returns the current rotation direction
        '''
        return self.rotation_dir

    def can_rotate(self, board):
        ''' Parameters: board - type: Board object
            Return value: type : bool
            
            Checks if the shape can be rotated.
            
            1. Get the rotation direction using the get_rotation_dir method
            2. Compute the position of each block after rotation and check if
            the new position is valid
            3. If any of the blocks cannot be moved to their new position,
            return False
                        
            otherwise all is good, return True
        '''
        
        ####### MY CODE ######
        
        dir1 = self.get_rotation_dir()
        center = self.blocks[1]
        for block in self.blocks:
            x = center.x - (dir1 * center.y) + (dir1 * block.y)
            y = center.y + (dir1 * center.x) - (dir1 * block.x)
            if not board.can_move(x, y):
                return False
        return True

    def rotate(self, board):
        ''' Parameters: board - type: Board object

            rotates the shape:
            1. Get the rotation direction using the get_rotation_dir method
            2. Compute the position of each block after rotation
            3. Move the block to the new position
            
        '''    

        ####  MY CODE  #####
        
        dir1 = self.get_rotation_dir()
        center = self.blocks[1]
        for block in self.blocks:
            x = center.x - (dir1 * center.y) + (dir1 * block.y)
            y = center.y + (dir1 * center.x) - (dir1 * block.x)    
            block.move(x - block.x, y - block.y)

        ### This should be at the END of your rotate code. 
        ### DO NOT touch it. Default behavior is that a piece will only shift
        ### rotation direciton after a successful rotation. This ensures that 
        ### pieces which switch rotations definitely remain within their 
        ### accepted rotation positions.
        if self.shift_rotation_dir:
            self.rotation_dir *= -1

        

############################################################
# ALL SHAPE CLASSES
############################################################

 
class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, 'blue')
        self.shift_rotation_dir = True
        self.center_block = self.blocks[2]

class J_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, 'orange')        
        self.center_block = self.blocks[1]

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'cyan')        
        self.center_block = self.blocks[1]


class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x    , center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x   , center.y + 1),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'red')
        self.center_block = self.blocks[0]

    def rotate(self, board):
        # Override Shape's rotate method since O_Shape does not rotate
        return 

class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'green')
        self.center_block = self.blocks[0]
        self.shift_rotation_dir = True
        self.rotation_dir = -1


class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x    , center.y + 1)]
        Shape.__init__(self, coords, 'yellow')
        self.center_block = self.blocks[1]


class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y), 
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, 'magenta')
        self.center_block = self.blocks[1]
        self.shift_rotation_dir = True
        self.rotation_dir = -1      



############################################################
# BOARD CLASS
############################################################

class Board():
    ''' Board class: it represents the Tetris board

        Attributes: width - type:int - width of the board in squares
                    height - type:int - height of the board in squares
                    canvas - type:CanvasFrame - where the pieces will be drawn
                    grid - type:Dictionary - keeps track of the current state of
                    the board; stores the blocks for a given position

                    # optional ex
                    preview_board - type:PreviewBoard - where next piece will be drawn
                    score_board - type:ScoreBoard - where the score and level
                    will be drawn
                    points - type:int - keeps track of current score
                    level - type:int - keeps track of current level, max is 10
    '''
    
    def __init__(self, win, width, height):
        self.width = width
        self.height = height
        
        ####### MY CODE ######
        # optional ex
        self.points = 0
        self.level = 0

        # optional ex
        # create board to draw preview shape on
        self.preview_board = PiecePreview(win, width, height/6)
        
        # create a canvas to draw the tetris shapes on
        self.canvas = CanvasFrame(win, self.width * Block.BLOCK_SIZE,
                                        self.height * Block.BLOCK_SIZE)
        self.canvas.setBackground('light gray')
        
        # optional ex
        # create board to track the score and level
        self.score_board = ScoreBoard(win, width, height/6)
        
        # create an empty dictionary
        # currently we have no shapes on the board
        self.grid = {}

    def draw_shape(self, shape):
        ''' Parameters: shape - type: Shape
            Return value: type: bool

            draws the shape on the board if there is space for it
            and returns True, otherwise it returns False
        '''
        
        if shape.can_move(self, 0, 0):
            shape.draw(self.canvas)
            return True
        return False

    def can_move(self, x, y):
        ''' Parameters: x - type:int
                        y - type:int
            Return value: type: bool

            1. check if it is ok to move to square x,y
            if the position is outside of the board boundaries, can't move there
            return False

            2. if there is already a block at that postion, can't move there
            return False

            3. otherwise return True
            
        '''
            
        ####### MY CODE ######
        
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return False
        elif (x, y) in self.grid.keys():
            return False
        return True

    def add_shape(self, shape):
        ''' Parameter: shape - type:Shape
            
            add a shape to the grid, i.e.
            add each block to the grid using its
            (x, y) coordinates as a dictionary key

            Hint: use the get_blocks method on Shape to
            get the list of blocks
            
        '''
        
        ####### MY CODE ######
        
        for block in shape.get_blocks():
            self.grid[(block.x, block.y)] = block

    def delete_row(self, y):
        ''' Parameters: y - type:int

            remove all the blocks in row y
            to remove a block you must remove it from the grid
            and erase it from the screen.
            If you dont remember how to erase a graphics object
            from the screen, take a look at the Graphics Library
            handout
            
        '''
        
        ####### MY CODE ######
        
        for i in range(self.width):
            self.grid[(i, y)].undraw()
            del self.grid[(i, y)]
            
    def is_row_complete(self, y):        
        ''' Parameter: y - type: int
            Return value: type: bool

            for each block in row y
            check if there is a block in the grid (use the in operator) 
            if there is one square that is not occupied, return False
            otherwise return True
            
        '''
        
        ####### MY CODE ######
        
        for i in range(self.width):
            if (i, y) not in self.grid.keys():
                return False
        return True
    
    def move_down_rows(self, y_start):
        ''' Parameters: y_start - type:int                        

            for each row from y_start to the top
                for each column
                    check if there is a block in the grid
                    if there is, remove it from the grid
                    and move the block object down on the screen
                    and then place it back in the grid in the new position

        '''
        
        ####### MY CODE ######
        
        for row in reversed(range(y_start+1)):
            for column in range(self.width):
                if (column, row) in self.grid.keys():
                    self.grid[(column, row)].move(0, +1)
                    self.grid[(column, row+1)] = self.grid[(column, row)]
                    del self.grid[(column, row)]
                    
    def remove_complete_rows(self):
        ''' removes all the complete rows
            1. for each row, y, 
            2. check if the row is complete
                if it is,
                    delete the row
                    move all rows down starting at row y - 1
            3. add 10 points for each complete row,
            if 4 complete rows add 10 bonus points
            4. goes up one level for each 100 points, up to 10

        '''
        
        ####### MY CODE ######
        
        count = 0
        for y in range(self.height):
            if self.is_row_complete(y):
                self.delete_row(y)
                self.move_down_rows(y - 1)
                count +=1
                
        # optional ex
        # add points
        if count > 0:
            self.points += count*10
            if count == 4:
                self.points += 10
            self.score_board.set_points(self.points)
        # update level
        if self.level < 5:
            self.level = self.points / 100
            self.score_board.set_level(self.points/100)

    def game_over(self):
        ''' display "Game Over !!!" message in the center of the board
            HINT: use the Text class from the graphics library
        '''
        
        ####### MY CODE ######
        
        p = Point((self.width * Block.BLOCK_SIZE) / 2,\
                 (self.height * Block.BLOCK_SIZE) / 2)
        GO = Text(p, "GAME OVER !!!")
        GO.draw(self.canvas)
        GO.setSize(25)
        GO.setStyle("bold")

    ####### MY CODE ######
    # optional ex
    def pause(self):
        ''' display "PAUSE" message in the center of the board'''
        p = Point((self.width * Block.BLOCK_SIZE) / 2,\
                 (self.height * Block.BLOCK_SIZE) / 2)
        self.pause = Text(p, "PAUSE")
        self.pause.draw(self.canvas)
        self.pause.setSize(25)
        self.pause.setStyle("bold")
        
    # optional ex
    def unpause(self):
        ''' remove "PAUSE" message from the board '''
        self.pause.undraw()
        

############################################################
# CLASSES FOR OPTIONAL EXERCISE
############################################################

class ScoreBoard():
    ''' ScoreBoard class: represents the Tetris score board

        Attributes: width - type:int - width of the board in squares
                    height - type:int - height of the board in squares
                    canvas - type:CanvasFrame - where the score will be drawn
                    points - type:Text - points to draw
                    level - type:Text - level to draw
    '''
    def __init__(self, win, width, height):
        self.width = width
        self.height = height
        self.canvas = CanvasFrame(win, self.width * Block.BLOCK_SIZE,
                                  self.height * Block.BLOCK_SIZE)
        self.canvas.setBackground('light gray')
        self.points = Text(Point(self.canvas.width*0.75, self.canvas.height*0.25), 0)
        self.level = Text(Point(self.canvas.width*0.75, self.canvas.height*0.75), 0)
        
        self.draw()

    def draw_boxes(self):
        point_box = Rectangle(Point(self.canvas.width*0.65, self.canvas.height*0.15),\
                             Point(self.canvas.width*0.85, self.canvas.height*0.35))
        point_box.setFill("black")
        
        level_box = Rectangle(Point(self.canvas.width*0.65, self.canvas.height*0.65),\
                             Point(self.canvas.width*0.85, self.canvas.height*0.85))
        level_box.setFill("black")
        
        point_box.draw(self.canvas)
        level_box.draw(self.canvas)
        
    def draw_text(self):
        point_text = Text(Point(self.canvas.width*0.25, self.canvas.height*0.25), "SCORE:")
        point_text.setStyle("bold")

        level_text = Text(Point(self.canvas.width*0.25, self.canvas.height*0.75), "LEVEL:")
        level_text.setStyle("bold")
        
        point_text.draw(self.canvas)
        level_text.draw(self.canvas)

    def draw_points(self):
        self.points.setFill("white")
        self.points.setStyle("bold")
        self.points.draw(self.canvas)

    def draw_level(self):
        self.level.setFill("white")
        self.level.setStyle("bold")
        self.level.draw(self.canvas)

    def draw(self):
        ''' draws everything on the board '''
        self.draw_boxes()
        self.draw_text()
        self.draw_points()
        self.draw_level()
    
    def set_points(self, n):
        ''' Parameter: n - type: int - new points

            sets points
        '''
        self.points.setText(str(n))

    def set_level(self, n):
        ''' Parameter: n - type: int - new level

            sets level
        '''
        self.level.setText(str(n))

class PiecePreview():
    ''' PiecePreview class: represents the Tetris shape preview board

        Attributes: width - type:int - width of the board in squares
                    height - type:int - height of the board in squares
                    canvas - type:CanvasFrame - where the shape will be drawn
    '''
    def __init__(self, win, width, height):
        self.width = width
        self.height = height
        self.canvas = CanvasFrame(win, self.width*Block.BLOCK_SIZE,
                                  self.height*Block.BLOCK_SIZE)
        self.canvas.setBackground('light gray')

    def draw_preview(self, shape):
        ''' Parameter: shape - type:Shape - shape to draw on the board

            draws the shape on the board
        '''
        shape.draw(self.canvas)


############################################################
# TETRIS CLASS
############################################################

class Tetris():
    ''' Tetris class: Controls the game play
        Attributes:
            SHAPES - type: list (list of Shape classes)
            DIRECTION - type: dictionary - converts string direction to (dx, dy)
            BOARD_WIDTH - type:int - the width of the board
            BOARD_HEIGHT - type:int - the height of the board
            board - type:Board - the tetris board
            win - type:Window - the window for the tetris game
            delay - type:int - the speed in milliseconds for moving the shapes
            current_shapes - type: Shape - the current moving shape on the board

            # optional ex
            preview_shapes - type: Shape - the preview shape on the board
            pause - type:Boolean - pause status. True - game pause, False otherwise
    '''
    
    SHAPES = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
    DIRECTION = {'Left':(-1, 0), 'Right':(1, 0), 'Down':(0, 1)}
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20
    
    def __init__(self, win):
        self.board = Board(win, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        self.win = win
        self.delay = 1000 #ms

        # optional ex
        ####  MY CODE ####
        self.pause = False

        # sets up the keyboard events
        # when a key is called the method key_pressed will be called
        self.win.bind_all('<Key>', self.key_pressed)

        # set the current shape to a random new shape
        self.current_shape = self.create_new_shape()

        # optional ex
        # set the preview shape to a random new shape
        ####  MY CODE ####
        self.preview_shape = self.create_new_shape()

        # Draw the current_shape oan the board (take a look at the
        # draw_shape method in the Board class)
        ####  MY CODE ####
        self.board.draw_shape(self.current_shape)

        # optional ex
        # draw the preview shape
        self.board.preview_board.draw_preview(self.preview_shape)
        
        # For Step 9:  animate the shape!
        ####  MY CODE ####
        self.animate_shape()

    def create_new_shape(self):
        ''' Return value: type: Shape
            
            Create a random new shape that is centered
             at y = 0 and x = int(self.BOARD_WIDTH/2)
            return the shape
        '''
        
        ####  MY CODE ####
        rand_shape = random.choice(self.SHAPES)
        y = 0
        x = int(self.BOARD_WIDTH / 2)
        center = Point(x, y)
        shape = rand_shape(center)
        
        return shape
    
    def animate_shape(self):
        ''' animate the shape - move down at equal intervals
            specified by the delay attribute
            delay decreases with higher level
        '''

        # optional ex
        ####  MY CODE ####
        if not self.pause:
            if self.board.level == 1:
                self.delay = 900
            if self.board.level == 2:
                self.delay = 800
            if self.board.level == 3:
                self.delay = 700
            if self.board.level == 4:
                self.delay = 600
            if self.board.level == 5:
                self.delay = 500
                
            self.do_move('Down')
            self.win.after(self.delay, self.animate_shape)
    
    def do_move(self, direction):
        ''' Parameters: direction - type: string
            Return value: type: bool

            Move the current shape in the direction specified by the parameter:
            First check if the shape can move. If it can, move it and return True
            Otherwise if the direction we tried to move was 'Down',
            1. add the current shape to the board
            2. remove the completed rows if any 
            3. create a new random shape and set current_shape attribute
            4. If the shape cannot be drawn on the board, display a
               game over message

            return False

        '''
        
        ####  MY CODE ####
        
        if not self.pause:
            dir_pos = self.DIRECTION[direction]
            x = dir_pos[0]
            y = dir_pos[1]
            
            # move shape if can
            if self.current_shape.can_move(self.board, x, y):
                self.current_shape.move(x, y)
                return True
            
            # if shape can't move when pressed 'down'
            elif direction == "Down":
                # add the last shape to board.grid
                self.board.add_shape(self.current_shape)
                # remove the complete rows, if any
                self.board.remove_complete_rows()
                # set current shape receive the preview shape
                self.current_shape = self.preview_shape
                
                # game over if no place on board
                if not self.current_shape.can_move(self.board, 0, 0):
                    self.board.game_over()
                else:
                    # undraw the preview shape from the preview board
                    self.preview_shape.undraw()
                    # draw the current shape on the board
                    self.board.draw_shape(self.current_shape)
                    # receive a new preview shape
                    self.preview_shape = self.create_new_shape()
                    # draw the new preview shape on the preview board
                    self.board.preview_board.draw_preview(self.preview_shape)
                    
            return False

    def do_rotate(self):
        ''' Checks if the current_shape can be rotated and
            rotates if it can
        '''
        
        ####  MY CODE ####
        
        if self.current_shape.can_rotate(self.board):
            self.current_shape.rotate(self.board)
    
    def key_pressed(self, event):
        ''' this function is called when a key is pressed on the keyboard
            it currenly just prints the value of the key

            Modify the function so that if the user presses the arrow keys
            'Left', 'Right' or 'Down', the current_shape will move in
            the appropriate direction

            if the user presses the space bar 'space', the shape will move
            down until it can no longer move and is added to the board

            if the user presses the 'Up' arrow key ,
                the shape should rotate.

        '''
            
        #### MY CODE ####

        # key is receiving the string value of the key pressed
        key = event.keysym
        
        # move the piece to floor
        if key == "space" and not self.pause:
            while self.current_shape.can_move(self.board, 0, 1):
                self.do_move("Down")
            self.do_move("Down")
            
        # rotate the piece
        elif key == "Up" and not self.pause:
            self.do_rotate()
            
        elif key == 'p' or key == 'P':
            if not self.pause:
                # pause the game and draw the pause message
                Board.pause(self.board)
                self.pause = True
            else:
                # unpause the game and undraw the message.
                Board.unpause(self.board)
                self.pause = False
                self.animate_shape()
                
        # do other moves
        else:        
            self.do_move(key)
       
################################################################
# Start the game
################################################################

win = Window("Tetris")
game = Tetris(win)
win.mainloop()
