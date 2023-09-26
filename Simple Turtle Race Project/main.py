from turtle import Turtle, Screen
import random


# TODO: etch a sketch app
# w key = move forward, s key = backwards, a = counter-clockwise, d = clockwise
# def move_forward():
#     tim.forward(50)
#
#
# def move_backward():
#     tim.back(50)
#
#
# def counter_clockwise():
#     tim.left(10)
#
#
# def clock_wise():
#     tim.right(10)
#
#
# def clear():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clock_wise)
# screen.onkey(key=" ", fun=clear)


# TODO: turtle race
is_race_on = False
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="which turtle will win the race? enter a color: ")
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-90 + turtle_index * 30)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The winning turtle is {winning_color}")
            else:
                print(f"You have lost! The winning turtle is {winning_color}")

screen.listen()
screen.exitonclick()