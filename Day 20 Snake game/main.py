import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

score = []

screen = Screen()
# creating a screen size and give it a title
screen.screensize(canvwidth=800, canvheight=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision of the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #dection collision of the walls
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or  snake.head.ycor() < -380:
        game_is_on = False
        score.resets()
        score.game_over()

    #dection collision pf tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.resets()
            score.game_over()
    #teleport  the snake if it comes near wall
    # if snake.head.xcor() > 299:
    #     snake.teleport(x=-299, y=0)  # Assuming you're using the wrapping approach
    # elif snake.head.xcor() < -299:
    #     snake.teleport(x=299 ,y=0)
        # score += 1
        # print(f"your score is {score}")
#these were my solution to create three turtles.
# head = Turtle(shape="square")
# head.color("gray")
# head.goto(x=0,y=0)
#
# stomach = Turtle(shape="square")
# stomach.penup()
# stomach.goto(x=-20, y=0)
# stomach.color("gray")
#
# tail = Turtle(shape="square")
# tail.penup()
# tail.goto(x=-40, y=0)
# tail.color("gray")
screen.exitonclick()
