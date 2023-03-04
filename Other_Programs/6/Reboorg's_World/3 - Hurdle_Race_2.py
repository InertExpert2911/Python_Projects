# Access the below link to run the code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Function to jump
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# ------------------------------------------------------------------------------------------------------

# METHOD - 1:

# Use while loop to check if the condition at_goal() (a boolean) and jump
# If at goal no need to jump, if not at_goal() then continue to jump
# Eg: at_goal() == False then, not at_goal() will be true (LOGICAL OPERATOR: AND, OR and NOT)
while not at_goal():
    jump()

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------

# METHOD - 2:

# at_goal() holds booleans True or False
# while at_goal() == False:
#     jump()

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------

# METHOD - 3:

# at_goal() holds booleans True or False
# while at_goal() != True:
#     jump()

# ------------------------------------------------------------------------------------------------------
