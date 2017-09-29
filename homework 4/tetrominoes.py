#Denis Savenkov
#tetrominoes.py

from graphics import *

class Block(Rectangle):
    def __init__(self, pos, color):
        self.x = pos.x
        self.y = pos.y
        Rectangle.__init__(self, Point(pos.x*30, pos.y*30),\
                           Point(pos.x*30 + 30, pos.y*30 + 30))
        self.setFill(color)
        self.setWidth(3)

class Shape:
    def __init__(self, pos_list, color):
        self.block_list = []
        for pos in pos_list:
            self.block_list.append(Block(pos, color))

    def draw(self, win):
        for block in self.block_list:
            block.draw(win)

class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x-2, center.y),\
                  Point(center.x-1, center.y),\
                  Point(center.x, center.y),\
                  Point(center.x+1, center.y)]
        Shape.__init__(self, coords, "blue")

class J_shape(Shape):
    def __init__(self, center):
        coords=[Point(center.x-1, center.y),\
                Point(center.x, center.y),\
                Point(center.x+1, center.y),\
                Point(center.x+1, center.y+1)]
        Shape.__init__(self, coords, "orange")

class L_shape(Shape):
    def __init__(self, center):
        coords=[Point(center.x-1, center.y+1),\
                Point(center.x-1, center.y),\
                Point(center.x, center.y),\
                Point(center.x+1, center.y)]
        Shape.__init__(self, coords, "cyan")

class O_shape(Shape):
    def __init__(self, center):
        coords=[Point(center.x-1, center.y+1),\
                Point(center.x-1, center.y),\
                Point(center.x, center.y),\
                Point(center.x, center.y+1)]
        Shape.__init__(self, coords, "red")

class S_shape(Shape):
    def __init__(self, center):
        coords=[Point(center.x-1, center.y+1),\
                Point(center.x ,center.y+1),\
                Point(center.x, center.y),\
                Point(center.x+1, center.y)]
        Shape.__init__(self, coords, "green")

class T_shape(Shape):
    def __init__(self, center):
        coords=[Point(center.x-1, center.y),\
                Point(center.x, center.y+1),\
                Point(center.x, center.y),\
                Point(center.x+1, center.y)]
        Shape.__init__(self, coords, "yellow")

class Z_shape(Shape):
    def __init__(self, center):
        coords=[Point(center.x-1, center.y),\
                Point(center.x, center.y+1),\
                Point(center.x, center.y),\
                Point(center.x+1, center.y+1)]
        Shape.__init__(self, coords, "magenta")

#block test
        
#win = GraphWin("Tetrominoes", 150, 150)
# the block is drawn at position (1, 1) on the board
#block = Block(Point(1, 1), "red")
# the __init__ method for your block should deal with converting
# the Point into pixels
#block.draw(win)
#win.mainloop()
    
#I_shape test

#win = GraphWin("Tetrominoes", 200, 150)
#shape = I_shape(Point(3, 1))
#shape.draw(win)
#win.mainloop()

#Shapes func

def main():
    win = GraphWin("Tetrominoes", 900, 150)
    # a list of shape classes
    tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape,\
                   T_shape, Z_shape]
    x=3
    for tetromino in tetrominoes:
        shape = tetromino(Point(x, 1))
        shape.draw(win)
        x += 4

    win.mainloop()

#run
main()
