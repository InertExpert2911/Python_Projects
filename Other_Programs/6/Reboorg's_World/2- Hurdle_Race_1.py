# Access the below link to run the code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Function that will help us to turn the robot right
# Reuse this function whenever needed. So, that we don't have to type turn_left() 3 times fro every right turn
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Define a function that performs the jump action
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

# Loop through the range 6 (0, 1, 2, 3, 4, 5) times to perform the action 6 times
for i in range(0, 6):
    jump()

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------

# METHOD - 2:

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#    jump()
#    number_of_hurdles -= 1
#    # print(number_of_hurdles) 

# ------------------------------------------------------------------------------------------------------
