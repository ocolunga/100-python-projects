import turtle as turtle_module
import random
from color_data import color_list

turtle_module.colormode(255)
turtle = turtle_module.Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
