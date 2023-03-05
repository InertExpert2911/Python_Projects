# Access the below link to run the code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Function to jump
def jump():
    turn_left()

    # A complex while indeed
    while wall_on_right() == True and front_is_clear() == True and at_goal() == False:
        move()

    # If right is clear, we want to turn right and move
    while right_is_clear() == True:
        turn_right()
        move()


# Loops until you reach the goal
while not at_goal():
    # front_is_clear() is a function to check if your front is clear or there is something in front
    if front_is_clear() == True:
        # Move() if nothing is in front
        move()
    # wall_in_front() is a function to check if a present in front
    elif wall_in_front() == True:
        # Using the above defined function to jump
        jump()

#---------------------------------------------------------------------------------------------

# METHOD - 1:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
    
# def jump():
#     turn_left()

#     while wall_on_right():
#         move()

#     turn_right()
#     move()
#     turn_right()
    
#     while front_is_clear():
#         move()
    
#     turn_left()
    
    
# while not at_goal():
#     if wall_in_front() == True:
#         jump()
#     else:
#         move()

# ----------------------------------------------------------------------------------------------

