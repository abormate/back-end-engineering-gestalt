# --------------------------------------- #
#
# -- Scope - Python StudySpace
#
# --------------------------------------- #

"""
Scope refers to where a variable or function name is available to be used. For example, 
when we create variables in a function (by giving names to our parameters for example), 
that data is not available outside of that function.

For example:

"""

def subtract(x, y):
    return x - y
result = subtract(5, 3)
# print(x)
# ERROR! "name 'x' is not defined"

"""
When the subtract function is called, we assign the variable x to 5, but x only exists in the code 
within the subtract function. If we try to print x outside of that function, then we won't get a 
result. In fact, we'll get a big fat error.

"""

# ------------------------------ #
# -- Assignment -- Practice
# ------------------------------ #

# Find the bug in the code on line 10. We're using variable names from the wrong scope. Fix it!

# ------------------------------ #
# -- Buggy Code --
# ------------------------------ #

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

# max_health = get_max_health(modifier, level)

# don't touch below this line

# print(f"max_health is: {max_health}")

# ------------------------------ #
# -- Fixed Code --
# ------------------------------ #

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")

