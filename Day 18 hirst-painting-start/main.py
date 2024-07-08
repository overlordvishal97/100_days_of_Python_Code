###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# Creating a million dollar art of a known artist
import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors[2:])

t.colormode(255)
tim = t.Turtle()
tim.speed("fast")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors[2:]))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
