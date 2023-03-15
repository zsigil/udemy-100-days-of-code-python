from turtle import Turtle
import random

COLORS = ["red", "orange", "grey", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.create_cars()
        self.car_speed_factor = 1
    

    def create_cars(self):
        for color in COLORS:
            color_index = COLORS.index(color)
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(color)
            new_car.setheading(180)
            new_car.goto(270-random.randint(0, 500),250-color_index*90)
            self.cars.append(new_car)


    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT*self.car_speed_factor)
            car_x, car_y = car.pos()
            if car_x < -280:
                car.setx(270)
    

    def get_car_coordinates(self):
        car_coords = []
        for car in self.cars:
            car_coords.append(car.pos())
        return car_coords
    

    def increase_speed(self):
        self.car_speed_factor *= 1.2


            


