from turtle import  Turtle,Screen

class Paddle(Turtle):
    def __init__(self,postion,shape):
        super().__init__()
        self.shape(shape)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(postion)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

