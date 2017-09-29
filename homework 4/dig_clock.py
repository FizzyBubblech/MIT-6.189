#Denis Savenkov
#dig_clock.py

from graphics import *

# create the graphics window
#new_win = GraphWin("Digital Clock", 300, 300)
# create a text objects centered at (100, 100)
#msg1 = Text( Point( 100, 100 ), "Hello, world!" )
#msg1.draw( new_win )
#msg1.setSize(25)
#msg1.setStyle("bold")
#msg1.setTextColor("red")
# process events
#new_win.mainloop()

class DigitalClock:
    def __init__(self, win, hour=0, minute=0, second=0, color="dark green"):
        assert (0 <= hour < 24) and (0 <= minute < 60) and (0 <= second < 60)
        
        self.win = win
        self.hour = hour
        self.minute = minute
        self.second = second
        self.time = Text(Point(0.5*win.width, 0.5*win.height), self.convert_to_regular())

        self.draw(color)
        self.animate()

    def convert_to_regular(self):
        t = "AM"
        hour = self.hour
        if self.hour == 0:
            hour = 12
        if self.hour == 12:
            t = "PM"
        if self.hour > 12:
            t = "PM"
            hour = self.hour - 12
        str_time = str(hour) + ":" + str(self.minute) + ":" + str(self.second), t
        return str_time

    def convert_to_seconds(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self):
        seconds = self.convert_to_seconds()
        seconds += 1

        hour = seconds // 3600
        if hour > 23:
            self.hour = hour - 24
        else:
            self.hour = hour
        self.minute = (seconds%3600) // 60
        self.second = seconds%60
        self.time.setText(self.convert_to_regular())

    def animate(self):
        self.increment()
        self.win.after(1000, self.animate)
    
    def draw_face(self, color):
        p1 = Point(0.1*self.win.width, 0.1*self.win.height)
        p2 = Point(0.9*self.win.width, 0.9*self.win.height)
        box = Rectangle(p1, p2)
        box.draw(self.win)
        box.setFill(color)
        box.setOutline("black")
        box.setWidth(5)

    def draw_text(self):
        self.time.draw(self.win)
        self.time.setSize(25)
        self.time.setStyle("bold")

    def draw(self, color):
        self.draw_face(color)
        self.draw_text()

    def __str__(self):
        return str(self.hour) + ":" +str(self.minute) + ":" +str(self.second)


new_win = GraphWin("Digital Clock", 300, 300)
clock = DigitalClock(new_win)
new_win.mainloop()
