# ------------------------------------- #
#
# -- Boolean Logic -- 
#
# ------------------------------------- #

"""
Boolean logic refers to logic dealing with boolean (True or False) values. For 
example,

Dogs must have four legs and weigh less than 100 kilograms. (Both conditions must 
be true)

"""

# ----------------------------- #
# -- Logical Operators Review --
# ----------------------------- #

"""
As we discussed earlier, the logical operators and and or can be used to perform 
boolean logic.

"""

# ---------------------------- #
# -- AND Review --
# ---------------------------- #

"""
The and operator returns True if both of the conditions on either side evaluates to 
True:

"""

def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100

