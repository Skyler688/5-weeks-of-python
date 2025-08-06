# python3 week-2/instances-state-and-higher-order-functions-day19/turtle-race/main.py

# Note -> I took a slightly diferent aproach to the problem, I wanted to see if
# i could solve the problem without folowing the tutorial, and i landed on using a dict
# to dinamicaly create instances of each racer, instead of the arrays used in the tutorial.

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# create a dict and dinamicaly create each racer
racers = {}
spacing = 25 
start_pos = (len(colors) * spacing) / 2 # this gives me the starting position based on the spacing and number or racers

for index, color in enumerate(colors):
    turtle = Turtle(shape="turtle") # create a instanceof the Turtle object
    turtle.color(colors) # set color of racer
    turtle.penup() # disable drawing
    turtle.goto(x=-230, y=start_pos - (spacing * index)) # place each turtle evenly spaced within the starting range
    racers[colors] = turtle # save turtle instance in the dict


is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for color in colors:
        moove = random.randint(0, 10)
        racers[color].forward(moove)

        if racers[color].xcor() >= 230:
            is_race_on = False
            winner = color
            break
         
print(f"The winner is {color}")         

screen.exitonclick()