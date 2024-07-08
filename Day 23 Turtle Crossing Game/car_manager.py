import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import  Turtle

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.setheading(0)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(a=-250, b=250)
            new_car.penup()
            new_car.goto(300,y=random_y)
            self.all_cars.append(new_car)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)