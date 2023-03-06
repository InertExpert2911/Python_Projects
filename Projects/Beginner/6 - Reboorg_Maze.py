# Access the below link to run the code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Loop till you reach the goal
while not at_goal():
    # If right is clear, then turn right and move
    if right_is_clear():
        turn_right()
        move()
    # Else if front is clear, move forward
    elif front_is_clear():
        move()
    # If none of the above cases satisfy, then turn left
    else:
        turn_left()
