import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "orange", "blue", "green", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# creating no of turtles to race
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! The {winning_color} turtle is the winner")
            else:
                print(f"you lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

# orange = Turtle(shape="turtle")
# orange.color(colours[1])
# orange.penup()
# orange.goto(x=-230,y=50)
#
# yellow = Turtle(shape="turtle")
# yellow.color(colours[4])
# yellow.penup()
# yellow.goto(x=-230,y=-70)
#
# green =Turtle(shape="turtle")
# green.color(colours[3])
# green.penup()
# green.goto(x=-230,y=-40)
#
# blue = Turtle(shape="turtle")
# blue.color(colours[2])
# blue.penup()
# blue.goto(x=-230,y=-10)
#
# purple = Turtle(shape="turtle")
# purple.color(colours[5])
# purple.penup()
# purple.goto(x=-230,y=20)
