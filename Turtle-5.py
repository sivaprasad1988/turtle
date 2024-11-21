from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed('fastest')
turtle.color('red')


def random_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return (R, B, B)


def draw_circle(num_of_times,shifting_value=.5):
    """
    Draw a circle
    :param num_of_times: number of times circle should be dran
    :param shifting_value: Number to be shifted after reach circle
    """
    initial_heading = 0
    # Draw a circle
    for _ in range(num_of_times):
        turtle.color(random_color())
        current_heading = turtle.heading() + initial_heading
        turtle.setheading(current_heading)
        turtle.circle(100)
        initial_heading = initial_heading + shifting_value


draw_circle(1000)

screen = Screen()
screen.exitonclick()
