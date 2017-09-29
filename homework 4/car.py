#Denis Savenkov
#car.py

from graphics import *
from wheel import *

#rectangle ex

#new_win = GraphWin("A Car", 300, 300)
#rect = Rectangle(Point(10, 10), Point(200, 100))
#rect.setFill("blue")
#rect.setOutline("black")
#rect.setWidth(5)
#rect.draw(new_win)
#new_win.mainloop()

#define Car class
class Car:
    #define initilization method 
    def __init__(self, p1, r1, p2, r2, h):
        #wheels
        self.wheel1 = Wheel(p1, 0.6*r1, r1)
        self.wheel2 = Wheel(p2, 0.6*r2, r2)
        #body
        self.rectangle = Rectangle(Point(p1.x, p1.y-h), p2)
    #define draw method
    def draw(self, win):
        #draw body
        self.rectangle.draw(win)
        #draw wheels
        self.wheel1.draw(win)
        self.wheel2.draw(win)
    #define coloring method
    def set_color(self, wheel_color, tire_color, body_color):
        #wheel colors
        self.wheel1.set_color(wheel_color, tire_color)
        self.wheel2.set_color(wheel_color, tire_color)
        #body color
        self.rectangle.setFill(body_color)
    #move method
    def move(self, dx, dy):
        #move wheels
        self.wheel1.move(dx, dy)
        self.wheel2.move(dx, dy)
        #move body
        self.rectangle.move(dx, dy)
    #animation method
    def animate(self, win, dx, dy, n):
        if n > 0:
            #move car
            self.move(dx, dy)
            #repeat
            win.after(100, self.animate, win, dx, dy, n-1)

#animated car function
def car_go():
    #create window
    new_win = GraphWin("A Car", 700, 300)
    #create car object
    car1 = Car(Point(100, 100), 30, Point(300, 100), 30, 80)
    car1.draw(new_win)
    #set colors
    car1.set_color("black", "grey", "pink")
    #make it move
    car1.animate(new_win, 1, 0, 200)
    new_win.mainloop()

#call the func
car_go()
