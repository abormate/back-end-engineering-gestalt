# ---------------------------------------- #
#
# -- Variables Global Scope -- Python StudySpace
#
# ---------------------------------------- #

"""
So far we've been working in the global scope. That means that when we define a 
variable or a function, that name is accessible in every other place in our program,
even within other functions.

For example:

"""

pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius


"""
Because pi was declared in the parent "global" scope, it is usable within the 
get_area_of_circle() function.

"""