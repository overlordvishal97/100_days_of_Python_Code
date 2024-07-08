from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Makes the snake move"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self,positions):
        new_segments = Turtle(shape="square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(positions)
        self.segments.append(new_segments)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            mew_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(mew_x, new_y)
        self.head.forward(MOVE_DISTANCE)
# north
    def up(self):
        # if self.head.heading() != DOWN:
        self.head.setheading(UP)
#south
    def down(self):
        # if self.head.heading() != UP:
        self.head.setheading(DOWN)
#east
    def left(self):
        # if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)
#west
    def right(self):
        #if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)

    def teleport(self, x, y):
        self.head.goto(x, y)