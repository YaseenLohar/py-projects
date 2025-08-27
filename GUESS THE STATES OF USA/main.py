#IMPORTS
from turtle import Turtle, Screen
import pandas as pd

#SETUP
screen = Screen()
screen.setup(width=800, height=600)
screen.title("GUESS THE STATES GAME")
tata = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
tata.shape(image)
states_data = pd.read_csv("50_states.csv")

#OBJECT FOR WORD PLACEMENT
tutu = Turtle()
tutu.color("black")
tutu.hideturtle()
tutu.penup()

#STATE NAMES
all_states = states_data.state.to_list()
guessed_states =[]

#EXIT FUNCTION
def states_missed():
    for x in range(len(guessed_states)-1) :
        all_states.pop(all_states.index(guessed_states[x]))
        last = pd.DataFrame(all_states)
        last.to_csv("ALL THE STATES YOU MISSED.csv", index=False)

#MAIN GAME LOOP
game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} states guessed", prompt="guess a state: ").title()
    if answer in all_states:
        X = states_data[states_data["state"] == answer].x.item()
        Y = states_data[states_data["state"] == answer].y.item()
        tutu.goto(X, Y)
        tutu.write(arg=answer, align="center", font=("Arial", 8, "normal"))
        guessed_states.append(answer)

    if answer == "Exit":
        game_is_on = False
        states_missed()

    if len(guessed_states) == len(all_states):
        tutu.goto(0, 0)
        tutu.write("CONGRATS ON GUESSING ALL THE STATES!!!", align="center", font=("Arial", 20, "normal"))
        game_is_on = False

screen.exitonclick()



