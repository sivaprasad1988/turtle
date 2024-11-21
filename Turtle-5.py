from turtle import Turtle, Screen
import random
turtle = Turtle()
turtle.speed('fastest')
#turtle.shape("turtle")
turtle.color('red')

initial_heading = 0

# Draw a square
for _ in range(500):
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R,B,G)
    current_heading = turtle.heading() + initial_heading
    turtle.setheading(current_heading)
    turtle.circle(100)
    initial_heading = initial_heading + 1




screen = Screen()
screen.exitonclick()
