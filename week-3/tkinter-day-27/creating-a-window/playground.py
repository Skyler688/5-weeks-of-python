# Unlimited args (*args)
def add(*args):
    # NOTE -> the data type is a Tuple, can be accessed like a list "args[0]", Tuples are immutable meaning you cannot change add or remove items once created.
    print(f"Tuple *args, from add(): {args}") # prints in (1, 2, 3, 4, 5) format
    sum = 0
    for arg in args:
        sum += arg

    return sum    

# **kwargs
def calculate(num, **kwargs):
    #NOTE -> the data type is a dict, can be accessed like "kwargs["key"]"

    num += kwargs["add"]
    num *= kwargs["multiply"]
    
    return num

# Key word args in a class
class Car:
    def __init__(self, **kw):
        # use .get instead of ["key"] to avoid run time errors, .get will return none if no value is passed.
        self.make = kw.get("make")
        self.model = kw.get("model")

        