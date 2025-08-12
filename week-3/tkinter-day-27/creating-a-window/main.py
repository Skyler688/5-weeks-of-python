# python3 week-3/tkinter-day-27/creating-a-window/main.py

# import tkinter
from tkinter import * # Warning -> importinng everything "*" should only be done if using lots of the lib
from playground import add, calculate, Car

window = Tk()

window.title("My tkinter app")
window.minsize(width=500, height=300)
window.config(padx=20, pady=30) # add bading around the window border

# Label
my_label = Label(text="This is a label", font=("Arial", 24, "bold")) # this is how you configure the label
my_label.grid(row=0, column=0) # to display it call the pack function

# change the label, NOTE -> both methods bellow do the same thing
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=50)

# Buttons
def button_clicked(): 
    # CHALANGE -> change the label text when the button is clicked
    my_label["text"] = input.get() # grab the input string
    

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# New Button
new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=10)
input.grid(row=2, column=3)

# Optinal args
def my_func(a=1, b=2, c=3): # setting default values, also applys to classes
    return a + b + c

print(my_func()) # if nothing is passed it will use the default values
print(my_func(a=5)) # or set a var to not use default

# Unlimited args (*args)
print(add(2,4,6,4,8,7,6,2,1)) # can take in unlimited args (see playground.py for more info)

# Key Word Args (**kwargs)
print(calculate(7, add=3, multiply=2))

# Key Word args in a class
my_car = Car(make="Subaru") # did not pass the model
print(my_car.model) # returns none instead of throwing a runtime error

window.mainloop()