from turtle import Screen, Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# TODO: create a snake body
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.butt = self.segments[len(self.segments)-1]

    def create_snake(self):
        for square in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=0 - 20 * square, y=0)
            self.segments.append(new_segment)

    def add_segment(self):
        add_segment = Turtle(shape="square")
        add_segment.penup()
        add_segment.color("white")
        x_butt = self.butt.xcor()
        y_butt = self.butt.ycor()
        add_segment.goto(x_butt-20, y_butt-20)
        self.segments.append(add_segment)

    def reset(self):
        for segemnt in self.segments:
            segemnt.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
