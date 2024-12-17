import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_df = pd.read_csv("50_states.csv")
all_states = states_df.state.to_list()
guessed_states: list = []

while len(guessed_states) < 50:
    answer_state = str(
        screen.textinput(
            title=f"{len(guessed_states)}/50 States Correct",
            prompt="What's another state's name?",
        )
    ).title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_df[states_df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
    t.write(answer_state)


screen.exitonclick()
