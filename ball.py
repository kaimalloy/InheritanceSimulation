# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5

    def __init__(self,x,y):
        Prey.__init__(self,x,y,Ball.radius*2,Ball.radius*2,5,5)
        self.randomize_angle()
        self._color = 'blue'
    
    def update(self,model):
        self.move()
    
    def display(self,canvas):
        x,y = self.get_location()
        width,height = self.get_dimension()
        canvas.create_oval(x-width/2, y-height/2, x+width/2, y+height/2, fill=self._color)
