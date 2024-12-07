from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
vertical_position = [-100, -60, -20, 30, 70, 110]
turtle_list = []

for turtle_color in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_color])
    turtle.goto(x=-230, y=vertical_position[turtle_color])
    turtle_list.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
