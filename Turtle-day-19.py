from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move():
    turtle.forward(10)
def back():
    turtle.backward(10)
def left():
    turtle.right(10)
def right():
    turtle.left(10)
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()