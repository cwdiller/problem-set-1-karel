#========================================================
# Filename: Karel_Newspaper.py
# 
# Your name:
# Who did you work with (if anyone)?:
# If you consulted AI, link to transcript:
# Estimate for time spent on this problem (in hrs)?:
#========================================================

# I've just laid out a basic starting function below. 
# While this problem is fairly simple, you should still practice
# the good habit of writing helper functions to decompose the problem
# into smaller pieces. I have provided you with a template for the
# main function and then 3 helping functions as outlined in the PDF

import karel

def main():
   move_to_newspaper() #these three are pretty simple, its just get it
   pick_up_paper()  #got it
   return_to_start()  #good

def move_to_newspaper():
    turn_right()  #left would be pretty useless, theres a wall
    move() # karel moves down
    turn_left() # karel faces the door
    for c in range(2): # karel moves two times forward
        move()

def pick_up_paper(): 
    move() # karel moves to the paper
    pick_beeper() # karel collects the paper
    turn_around() # karel turns around
    move() # karel returns to where she was before she picked up the paper

def return_to_start():
    for c in range (2): # karel moves to her original spot
        move()
    turn_right() #karel turns right
    move() #karel moves into the corner

def turn_right():
	for c in range(3): # c is the greatest letter
	    turn_left() # one right is three lefts of course

     
def turn_around():
    for c in range(2): # turns around
        turn_left()
