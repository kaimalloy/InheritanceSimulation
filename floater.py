# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5

    def __init__(self,x,y):
        Prey.__init__(self,x,y,self.radius*2,self.radius*2,5,5)
        self.randomize_angle()
        self._color = 'red'

    def update(self,model):
        if random() <= 0.3:
            self.set_angle(self.get_angle() + random() - 0.5)
            self.set_speed(self.get_speed() + random() - 0.5)
            if self.get_speed() < 3:
                self.set_speed(3)
            elif self.get_speed() > 7:
                self.set_speed(7)
        self.move()

    def display(self,canvas):
        x,y = self.get_location()
        width,height = self.get_dimension()
        canvas.create_oval(x-width/2, y-height/2, x+width/2, y+height/2, fill=self._color)
