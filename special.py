# Special is derived from Black_Hole and Simulton:
# It is a green circle that moves in a zig-zag pattern.
# It eats Prey when it is going upwards and ignores Prey
# when it is going downwards.

from prey import Prey
from math import pi
from blackhole import Black_Hole
from mobilesimulton import Mobile_Simulton



class Special(Black_Hole,Mobile_Simulton):
    cycles = 30

    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._speed = 5
        self.set_dimension(30, 30)
        self.set_angle(pi/4)
        self._color = 'green'
        self._eating = False
        self._counter = 0

    def update(self,model):
        if self._counter == self.cycles:
            self.set_angle(-self.get_angle())
            self._eating = not self._eating
            self._counter = 0
        else:
            self._counter += 1
        if self._eating:
            removal_set = model.find((lambda x: isinstance(x, Prey) and self.contains(x.get_location())))
            for sim in removal_set:
                model.remove(sim)
        self.move()
