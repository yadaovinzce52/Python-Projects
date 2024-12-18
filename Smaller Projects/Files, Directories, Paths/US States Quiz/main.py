import collections
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_set = set(states_data["state"].tolist())
guessed = set()

while len(guessed) != 50:
    answer = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another states's name?").title()
    if answer == "Exit":
        break

    if answer in states_set:
        guessed.add(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coord = states_data[states_data.state == answer]
        t.goto(int(coord.x), int(coord.y))
        t.write(answer)

# states to learn
states_to_learn = []
for state in states_set:
    if state not in guessed:
        states_to_learn.append(state)

data = pandas.DataFrame(states_to_learn)
data.to_csv("states_to_learn.csv")
