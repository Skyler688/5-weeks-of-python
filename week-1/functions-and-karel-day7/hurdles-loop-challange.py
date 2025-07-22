# this is code to run on the site provided in the lesson "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json"

def turn_around():
    for i in range(2):
        turn_left()
    
def turn_right():
    for i in range(3):
        turn_left()
        
def move_range(amount):
    for i in range(amount):
        move()
     
def check_left():
    turn_right()
    is_wall = wall_in_front()
    turn_around()
    turn_right()
    return is_wall
    
def jump(height):
    turn_left()
    move()
    
    wall = True
    while check_left():
        move()
        height = height + 1
        
    turn_right()
    move()
    turn_right()
    move_range(height)
    height = 1
    turn_left()
    
    
height = 1
while not at_goal():
    if wall_in_front():
        jump(height)
    else:
        move()