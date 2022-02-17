from turtle import Turtle, Screen

jimmy = Turtle()
# Prints the location where the object is stored.
print(jimmy)

# Change the shape of the turtle.
# Calling methods associated with the object.
jimmy.shapesize()

# Changes the shape of the pointer to a turtle.
# Calling methods associated with the object.
jimmy.shape("turtle")

# Change the color of the turtle.
# Calling methods associated with the object.
jimmy.color("Light Blue")

# Move the turtle forward by 100 paces.
# Calling methods associated with the object.
jimmy.forward(100)

my_screen = Screen()
# Tapping into the attribute of the object.
print(my_screen.canvheight)

# Getting access of the exitonclick() method from Screen class.
# Calling methods associated with the object.
my_screen.exitonclick()

# DOCUMENTATION: https://docs.python.org/3/library/turtle.html#
