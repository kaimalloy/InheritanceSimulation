# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    tbm = 30

    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._counter = 1
    
    def update(self,model):
        removal_set = Black_Hole.update(self, model)
        if removal_set:
            for num in range(len(removal_set)):
                self.change_dimension(1, 1)
            self._counter = 1
        elif self._counter == Pulsator.tbm:
            self.change_dimension(-1, -1)
            self._counter = 1
            x,y = self.get_dimension()
            if x == 0 and y == 0:
                model.remove(self)
        else:
            self._counter += 1

        return removal_set
