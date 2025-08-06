# python3 week-2/instances-state-and-higher-order-functions-day19/etch-a-sketch/main.py

from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()


def move_forward():
    cursor.forward(10)

def move_back():
    cursor.back(10)

def move_clockwize():
    cursor.right(11.25)

def move_counterclockwize():
    cursor.left(11.25)

def clear():
    cursor.reset()
    
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(move_clockwize, "d")
screen.onkey(move_counterclockwize, "a")
screen.onkey(clear, "c")

screen.exitonclick()