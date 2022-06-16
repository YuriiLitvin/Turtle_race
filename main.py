from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle():
    turtle = Turtle(shape="turtle")
    turtle.penup()
    return turtle


def create_turtle_list():
    turtles = []
    for new_color in colors:
        new_turtle = create_turtle()
        new_turtle.color(new_color)
        turtles.append(new_turtle)
    return turtles


def line_up_turtles(turtle_list):
    x_start = -225
    y_start = -100
    for turtle in turtle_list:
        turtle.setpos(x=x_start, y=y_start)
        y_start += 50
    return turtle_list


def race():
    lowest_speed = 1
    highest_speed = 20
    finish_xcor = 230
    is_finished = False
    turtles_lined = line_up_turtles(create_turtle_list())
    while not is_finished:
        for race_turtle in turtles_lined:
            race_turtle.forward(random.randint(lowest_speed, highest_speed))
            if race_turtle.xcor() > finish_xcor:
                # is_finished = True
                return race_turtle


def check_bet():
    race_winner = race()
    if race_winner.fillcolor() == user_bet.lower():
        result = "You win!"
    else:
        result = "You lose."
    print(f"{result} The winner is {race_winner.fillcolor()} turtle.")


check_bet()


screen.exitonclick()


# DONE: create a turtle list
# DONE: link each turtle different color
# DONE: create amount of turtles due to colors amount
# DONE: add turtles to the list
# DONE: line these turtle on the start line one by one
# DONE: make them move to the finish line with different speed on each step
# DONE: determine finish line (or distance to finish line)
# DONE: determine the values of highest and lowest speed values
