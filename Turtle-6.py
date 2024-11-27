
from turtle import Turtle, Screen
import random
color_list = [(253, 253, 252), (242, 244, 247), (241, 247, 243), (144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

turtle = Turtle()
turtle.shape("circle")
yvalue = -50
turtle.teleport(-200, -50)
turtle.penup()

for _ in range(0,10):
    for _ in range(10):
        color = random.choice(color_list)
        # Convert to valid turtle format (values between 0.0 and 1.0)
        normalized_color = tuple(c / 255 for c in color)
        turtle.dot(20, normalized_color);
        turtle.penup()
        turtle.fd(50);
    yvalue += 50
    turtle.teleport(-200, yvalue)

screen = Screen()
screen.exitonclick()
