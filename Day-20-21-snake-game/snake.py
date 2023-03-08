from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self) -> None:
        self.snake = []
        self.direction = "right"
        self.alive = True

        for i in range(3):
            snake_part = Turtle()
            snake_part.speed('fast')
            snake_part.penup()
            snake_part.shape('square')
            snake_part.color('white')
            snake_part.setx(-i*20)
            self.snake.append(snake_part)


    def move_head(self):
        head_pos = self.snake[0].pos()

        if self.direction == 'right':
            #check if x is possible
            if head_pos[0]+MOVE_DISTANCE >= 290:
                self.alive = False
            self.snake[0].goto(head_pos[0]+MOVE_DISTANCE, head_pos[1])

        elif self.direction == 'left':
            #check if x is possible
            if head_pos[0]-MOVE_DISTANCE <= -290:
                self.alive = False
            self.snake[0].goto(head_pos[0]-MOVE_DISTANCE, head_pos[1])

        elif self.direction == 'up':
            #check if y is possible
            if head_pos[1]+MOVE_DISTANCE >= 290:
                self.alive = False
            self.snake[0].goto(head_pos[0], head_pos[1]+MOVE_DISTANCE)

        elif self.direction == 'down':
            #check if x is possible
            if head_pos[1]-MOVE_DISTANCE <= -290:
                self.alive = False
            self.snake[0].goto(head_pos[0], head_pos[1]-MOVE_DISTANCE)

        if self.tail_hit_by_head():
            self.alive = False


    def move_snake(self):
        for i in range(len(self.snake)-1, -1, -1):
            if i == 0:
                self.move_head()
            else:
                self.snake[i].goto(self.snake[i-1].pos())


    def up(self):
        if self.direction == 'down':
            self.alive = False
        else:
            self.direction = 'up'


    def down(self):
        if self.direction == 'up':
            self.alive = False
        else:
            self.direction = 'down'
    

    def left(self):
        if self.direction == 'right':
            self.alive = False
        else:
            self.direction = 'left'


    def right(self):
        if self.direction == 'left':
            self.alive = False
        else:
            self.direction = 'right'


    def is_alive(self):
        return self.alive
    

    def add_segment(self):
            last_segment_pos = self.snake[-1].pos()
            snake_part = Turtle()
            snake_part.speed('fast')
            snake_part.penup()
            snake_part.shape('square')
            snake_part.color('white')
            snake_part.goto(last_segment_pos)
            self.snake.append(snake_part)

    
    def tail_hit_by_head(self):
        tail_positions = []
        for i in range(1, len(self.snake)):
            tail_positions.append(self.snake[i].pos())

        if self.snake[0].pos() in tail_positions:
            return True
        
        return False

