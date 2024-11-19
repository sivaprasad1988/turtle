from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color('red')
i = 0
# Draw a square
for _ in range(100):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
