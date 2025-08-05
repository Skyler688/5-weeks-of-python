# python3 week-2/object-oriented-programming-day16/main.py

# importing the Turtle and Screen objects from turtle.
from turtle import Turtle, Screen

jeff = Turtle()

jeff.shape("turtle")
jeff.color("blue")
jeff.forward(100)

screen = Screen()
print(screen.canvheight) # canvasheight is an examle of a attribute (a value in the object)

screen.exitonclick() # exitonclick() is an example of a method (a function in the object)