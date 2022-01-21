import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States guess game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

data_dict = data.to_dict()

state = data_dict["state"]
x = data_dict["x"]
y = data_dict["y"]

count = 0
guessed_state = []
game_is_on = True
missed_states = []


while count < 50 and game_is_on:
    answer = screen.textinput(title=f"{count}/50 states guessed", prompt="Whats another state?").title()

    for i in range(0, 50):
        if answer == "Exit":
            game_is_on = False

            break
        if answer == state[i]:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x[i], y[i])
            t.write(state[i])
            count += 1
            guessed_state.append(state[i])

for j in range(0, 50):
    if state[j] in guessed_state:
        pass
    else:
        missed_states.append(state[j])

    missed_data = pandas.DataFrame(missed_states)
    missed_data.to_csv("states_to_learn.csv")

screen.mainloop()
