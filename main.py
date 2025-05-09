import turtle
import pandas

FONT = ("Courier", 8, "bold")
ALREADY_GUESSED_FONT = ("Courier", 20, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
turtl = turtle.Turtle()
turtl.hideturtle()
turtl.penup()
turtl.goto(-100, 0)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in guessed_states:
        turtl.write(f"You already got {answer_state}.\nTry again!", font=ALREADY_GUESSED_FONT)
        continue

    if answer_state in all_states:
        turtl.clear()
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item(), font=FONT)
