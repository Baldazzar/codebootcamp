import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day25USGame/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.speed("fastest")

incorrect = turtle.Turtle()
incorrect.penup()
incorrect.hideturtle()
incorrect.speed("fastest")



correct_guesses = []

states_correct = 0
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?")
    answer = answer_state.title()
    incorrect.clear()
    states_data = pandas.read_csv("day25USGame/50_states.csv")
    states = states_data["state"].to_list()
    if answer == 'Exit':
        break
    if answer not in correct_guesses:
        if answer in states:
            states_correct += 1
            state_cor = states_data[states_data.state == answer]
            writer.goto(int(state_cor.x), int(state_cor.y))
            writer.write(answer, align="center", font=("Times New Roman", 10, "normal"))
            correct_guesses.append(answer)
        else:
            incorrect.goto(0, 400)
            incorrect.write("Invalid Guess", align="center", font=("Times New Roman", 20, "normal"))
            

for guessed_state in correct_guesses:
    states.remove(guessed_state)

states_to_learned = pandas.DataFrame(states)
states_to_learned.to_csv("day25USGame/States_to_learn.csv")
