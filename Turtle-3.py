from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

shapes = [3,4,5,6,7,8,9,10]

for shape in shapes:
    angle = 360 / shape
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R,B,G)
    for _ in range(shape):
        turtle.forward(100)
        turtle.rt(angle)
# Draw a square

screen = Screen()
screen.exitonclick()
