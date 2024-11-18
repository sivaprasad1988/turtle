from turtle import  Turtle,Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color('red')
i = 0
while i < 4:
    turtle.forward(100)
    turtle.rt(90)
    i +=1

screen = Screen()
screen.exitonclick()