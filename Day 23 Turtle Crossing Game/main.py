import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
LAST_POSITION = (0, 280)


turtle = Player()
score = Scoreboard()
cars = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(turtle.up,"w")
screen.onkey(turtle.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    #detect collision with car
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False
    # detect a successful crossing
    if turtle.is_at_finish():
        score.level_up()
        cars.speed_up()
        turtle.go_to_start()

screen.exitonclick()