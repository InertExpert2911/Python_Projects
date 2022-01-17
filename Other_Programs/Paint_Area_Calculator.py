# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.

import math

def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    total_cans_needed = math.ceil(num_of_cans)
    print(f"You'll need {total_cans_needed} cans of paint.")


h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=h, width=w, cover=coverage)