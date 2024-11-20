from turtle import Turtle, Screen
import random
turtle = Turtle()
turtle.shape("turtle")
turtle.color('red')
#turtle.speed(1)


angle_list = [turtle.right,turtle.lt]
random_movement_list = [turtle.forward,turtle.backward]
direction_list = [0,90,180,270,360]

turtle.pensize(12)   # from here on lines of width 10 are drawn
# Draw a square
for _ in range(100):
    current_movement = random.choice(angle_list)
    movement_list = random.choice(random_movement_list)
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R,B,G)
    current_movement(random.choice(direction_list))
    movement_list(50)



screen = Screen()
screen.exitonclick()
