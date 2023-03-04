# Access the below link to run the code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Create a function that to turn the robot around, it will ask the robot to turn left a couple of times
# We only have turn_left() function, Making use of this to ask our robot to turn around
def turn_around():
    turn_left()
    turn_left()

# Function to turn the robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Reboorg follows the below instructions and makes a small lap
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
