import turtle
import pandas
import sys


# TODO: background image
screen = turtle.Screen()
screen.title("US States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# TODO: extract data from csv
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
for i in range(50):
    states[i] = states[i].lower()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

US_states = {}
amt_of_states_correct = 0

for i in range(50):
    dictionary = {states[i]: [x_cor[i], y_cor[i]]}
    US_states.update(dictionary)

while amt_of_states_correct < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?")

    if answer_state in states:
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        x_cor = US_states[answer_state][0]
        y_cor = US_states[answer_state][1]
        state_name.goto(x_cor, y_cor)
        state_name.write(f"{answer_state}", align="center", font=('Arial', 10, 'normal'))
        amt_of_states_correct += 1
        answer_state = screen.textinput(title=f"{amt_of_states_correct}/50 States Correct",
                                        prompt="What's another state name?")

    elif answer_state == "exit":
        sys.exit("End of game")

    else:
        answer_state = screen.textinput(title=f"{amt_of_states_correct}/50 States Correct",
                                        prompt="What's another state name?")

screen.exitonclick()