from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color('black')
        self.setheading(90)
        self.goto(STARTING_POSITION)
    

    def move_up(self):
        x,y = self.pos()
        self.goto(x, y+MOVE_DISTANCE)

    
    def check_collision(self, car_coords):
        for coord in car_coords:
            if self.distance(coord) < 30:
                return True
        return False
    

    def crossed_street(self):
        x,y = self.pos()
        if y>= FINISH_LINE_Y:   
            self.goto(STARTING_POSITION)
            return True
        return False


