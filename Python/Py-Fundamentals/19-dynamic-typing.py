# -------------------------------------- #
#
# -- Dynamic Typing --
#
# -------------------------------------- #

"""
Python is dynamically typed. All this means is that a variable can store any type, and that type can change.

For example, if I make a number variable, I can later change that variable to a string:

This is valid:

"""

speed = 5
speed = "five"

# --------------------------- #
# -- Just because you can -- doesn't mean you should --
# --------------------------- #

"""
In almost all circumstances, it's a bad idea to change the type of a variable. The "proper" thing to do is to just create a new one. For example:

"""

speed = 5
speed_description = "five"


# --------------------------- #
# -- What if it weren't dynamically typed?
# --------------------------- #

"""
Statically typed languages like Go (which you'll learn in a later course) are statically typed instead of dynamically typed. In a statically typed language, 
if you try to assign a value to a variable of the wrong type, an error would crash the program.

If Python were statically-typed, the first example from before would crash on the second line, speed = "five". The computer would give an error along 
the lines of you can't assign a string value ("five") to a number variable (speed)

"""

