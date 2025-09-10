#====================================================
# Filename: Karel_Painting.py
# 
# Your name: Corbin Diller
# Who did you work with (if anyone)?: N/A
# If you consulted AI, link to transcript: N/A
# Estimate for time spent on this prob (in hrs)?: ~1.5
#====================================================

# I've just laid out a basic starting function below, but remember that you
# absolutely should define more helping functions to decompose the problem
# into smaller pieces! Here I'm leaving those pieces (and helper functions)
# up to you to design and name as you see fit. Don't forget comments!

import karel


def main():
    turn_around() #if karel is not facing west already, she will turn until she faces west

    while not_facing_north(): #if karel is not facing north, she will:
        if left_is_blocked(): #paint the wall if its on her left, otherwise she:
            paint()
        else:                 # will turn to the left and move forward one, and if there is a wall on her left she will paint it
            turn_left()
            move()
    if facing_north(): # if karel is facing north, she will go inside
        go_inside()

def paint():
    while left_is_blocked(): # if there is a wall on karel's left, she will:
        put_beeper() # paint the wall
        move() # move forward


def turn_right():
    for c in range(3): # c is the greatest letter
        turn_left() # one right is three lefts of course

     
def turn_around():
    while not_facing_west(): # turning left until facing west
        turn_left()

def go_inside():
    
    while facing_north():      # if karel is facing north, she will:
        if left_is_blocked(): # move along the wall until she reaches the door, where she will:
            move()
        else:                 # turn toward the door and go inside
            turn_left()
            move()
