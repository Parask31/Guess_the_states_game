import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States guess game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

all_state = data.state.to_list()

guessed_state = []
missed_states = []


while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 states guessed", prompt="Whats another state?").title()

    if answer == "Exit":
        missed_state_list = [state for state in all_state if state not in guessed_state]
        missed_data = pandas.DataFrame(missed_state_list)
        missed_data.to_csv("states_to_learn.csv")
        break

    if answer in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        guessed_state.append(answer)

screen.mainloop()
