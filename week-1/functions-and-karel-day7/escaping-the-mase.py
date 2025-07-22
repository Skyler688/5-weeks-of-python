# this is code to run on the site provided in the lesson "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# this will always check if there is an opening to the right
# if the robot misses the opening to the left it will find it on the way back
right_mooves = 0 # used to prevent the robot from going in a infinant right circle if there is space
while not at_goal():
    # if there is an opening to the right go into it
    if right_is_clear() and right_mooves < 4:
        turn_right() 
        move()
        right_mooves += 1
    # if nothing ahead and right is blocked or right mooves is 4 move forward    
    elif front_is_clear():
        move()
        right_mooves = 0
    # if blocked ahead and right turn left or right mooves is 4 turn left    
    else:
        turn_left()
        right_mooves = 0