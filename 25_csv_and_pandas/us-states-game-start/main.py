
import csv
import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US state game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_data = pd.DataFrame(missing_states)
        missing_data.to_csv("missing.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)