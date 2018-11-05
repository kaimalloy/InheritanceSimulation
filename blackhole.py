# Black_Hole is derived from Simulton only: it updates by finding/removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10

    def __init__(self,x,y):
        Simulton.__init__(self,x,y,self.radius*2,self.radius*2)
        self._color = 'black'

    def update(self,model):
        removal_set = model.find((lambda x: isinstance(x, Prey) and self.contains(x.get_location())))
        for sim in removal_set:
            model.remove(sim)
        return removal_set

    def display(self,canvas):
        x,y = self.get_location()
        width,height = self.get_dimension()
        canvas.create_oval(x-width/2, y-height/2, x+width/2, y+height/2, fill=self._color)

    def contains(self,xy):
        return self.distance(xy) <= self.get_dimension()[0]/2

