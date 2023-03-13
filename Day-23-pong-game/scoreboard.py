from turtle import Turtle

class ScoreBoard:
    def __init__(self) -> None:
        self.board = Turtle()
        self.board.color('white')
        self.board.hideturtle()
        self.board.penup()
        self.board.setpos(0, 270)
        self.score = [0,0]
        self.update()
        
    

    def score_left(self):
        self.score[0] += 1
        self.update()

    
    def score_right(self):
        self.score[1] += 1
        self.update()


    def update(self):
        self.board.clear()
        self.board.goto(-20, 250)
        self.board.write(f"{self.score[0]}:{self.score[1]}", font=('Courier', 30, 'bold'), align='center')
