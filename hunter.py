# Hunter is derived from the Mobile_Simulton/Pulsator classes: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    tbm = 30

    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        self._speed = 5
        self.randomize_angle()
    
    def update(self,model):
        removal_set = Pulsator.update(self, model)
        close_set = model.find((lambda x: isinstance(x, Prey) and self.distance(x.get_location()) <= 200))
        closest = None
        closest_dist = 201
        for sim in close_set:
            if self.distance(sim.get_location()) < closest_dist:
                closest = sim
                closest_dist = self.distance(sim.get_location())
        if closest is not None:
            sim_x,sim_y = closest.get_location()
            x,y = self.get_location()
            self.set_angle(atan2(sim_y-y,sim_x-x))
        self.move()
        return removal_set
