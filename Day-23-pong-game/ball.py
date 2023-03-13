from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.y_move = 5
        self.x_move = 5
        self.move_speed = 0.02


    def move(self):
        x,y = self.pos()
        self.setposition(x+self.x_move, y+self.y_move)
    

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.90


    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.02
        self.move()    

