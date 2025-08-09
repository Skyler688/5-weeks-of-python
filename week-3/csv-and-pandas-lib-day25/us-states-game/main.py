# python3 week-3/csv-and-pandas-lib-day25/us-states-game/main.py

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

img = "week-3/csv-and-pandas-lib-day25/us-states-game/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# grab data from the csv file, NOTE -> the long include path is because i am running the script from the home dir
state_data = pandas.read_csv("week-3/csv-and-pandas-lib-day25/us-states-game/50_states.csv")
answerd_states = []

while (len(answerd_states) < 50):
    answer = screen.textinput(title=f"{len(answerd_states)}/50 Guess A State", prompt="Enter a state").title() # take the user input and convert it to title case
    if answer in state_data.state.to_list() and answer not in answerd_states: # check if users answer matches state data
        print("state found")
        answerd_states.append(answer)
        state = state_data[state_data.state == answer] # grab the state row
        pos_x = int(state.x.iloc[0]) # grab position x into a int
        pos_y = int(state.y.iloc[0])  # and y
        
        # create a turtle object and set position and display name
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(pos_x, pos_y)

        state_name.write(state.state.iloc[0], align="center", font=("Arial", 12, "normal"))
    elif answer == "Exit":
        break    
    else:
        print("invalid")  

    print(answerd_states)      


# Challange -> create a .csv containing all the states that have not bean guessed
all_states = state_data.state.to_list()
unanswered_states = []

for state in all_states:
    if state not in answerd_states:
        unanswered_states.append(state)

unanswered = {
    "unanswered_states": unanswered_states
}        

unanswered_fram = pandas.DataFrame(unanswered)

unanswered_fram.to_csv("week-3/csv-and-pandas-lib-day25/us-states-game/unanswered_states.csv")

