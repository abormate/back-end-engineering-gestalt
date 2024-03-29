# --------------------------------------------- #
#
# -- Logical Operators -- 
#
# --------------------------------------------- #

"""
You're probably familiar with the logical operators AND and OR.

Logical operators deal with boolean values, True and False.

The logical AND operator requires that both inputs are True to return True. 
The logical OR operator only requires that at least one input is True to return 
True.

For example:

True AND True is True
True AND False is False
False AND False is False

True OR True is True
True OR False is True
False OR False is False

"""

# -------------------------- #
# Python Syntax
# -------------------------- #

print(True and True)
# prints True

print(True or False)
# prints True

# ------------------------- #
# Nest with Parenthesis
# ------------------------- #

# We can nest logical expressions using parentheses.

print((True or False) and False)

# First, we evaluate the expression in the parentheses, (True or False). It evaluates to True:

print(True and False)

# True and False evaluates to False:

print(False)

# So, print((True or False) and False) prints "False" to the console.