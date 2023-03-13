from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos) -> None:
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)
    

    def move_up(self):
        (x, y) = self.pos()
        self.setpos(x, y+20)


    def move_down(self):    
        (x, y) = self.pos()
        self.setpos(x, y-20)