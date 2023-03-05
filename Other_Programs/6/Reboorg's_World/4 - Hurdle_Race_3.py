# Access the below link to run the code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Same function to turn right as before
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Same function to jump, removed a starting move() function
# Needed only jump 
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

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

# --------------------------------------------------------------------------------------------

# METHOD - 1:
# while not at_goal():
#     if wall_in_front() == True:
#         jump()
#     else:
#         move()

# ----------------------------------------------------------------------------------------------
