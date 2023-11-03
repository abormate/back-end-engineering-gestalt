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
print(x)
# ERROR! "name 'x' is not defined"

"""
When the subtract function is called, we assign the variable x to 5, but x only exists in the code 
within the subtract function. If we try to print x outside of that function, then we won't get a 
result. In fact, we'll get a big fat error.

"""

# ------------------------------ #
# -- Assignment -- Practice
# ------------------------------ #

