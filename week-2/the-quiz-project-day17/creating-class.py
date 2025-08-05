# python3 week-2/the-quiz-project-day17/creating-class.py

# Creating a empty class
class User:
    pass # can be used to create a empty object without throwing an error (can also be used in functions)

# must create an instance of the class to use it
user_1 = User()

# can add vars to the class using dot notation
user_1.id = "1234"
user_1.username = "iAmBattman3000"

# The vars can be accessed through dot notation as well
print(user_1.username)

# NOTE -> the code above can be error prone, bellow is how to create a Constructor to prevent such potential problems.


# Constructor
class MyConstructors:
    # this function runs when creating a instance of the class object, usfull for creating a new dict or data set for each instance.
    def __init__(self):
        print("I am a init function in a class object")

# NOTE -> when the instance is created the init function exicutes
instance = MyConstructors()


# Attributes and Methods
class myAttributes:
    # attributs are vars or values in the object
    def __init__(self, somthing): # Constructor function
        self.somthing = somthing
        self.default = 0 # can also be declared at a default starting value, no nead to pass the value in

    # This is a Method that adds to default attribute
    def add_default(self, amount):
        self.default += amount
        return self.default

# Note we pass inthe value of somthing in the in the creat instance call, 5 in this case
example = myAttributes(5)

print(example.somthing)
print(f"value before Method function: {example.default}")
print(f"value after Method function: {example.add_default(10)}")



