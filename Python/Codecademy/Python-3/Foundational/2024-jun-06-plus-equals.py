# ---------------------------------------- #
#
# -- Codecademy -- Plus Equals --
#
# ---------------------------------------- #

"""
Python offers a shorthand for updating variables. When you have a 
number saved in a variable and want to add to the current value of 
the variable, you can use the += (plus-equals) operator.

"""

# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

"""
Above, we keep a running count of the number of miles a person has 
gone hiking over time. Instead of recalculating from the start, we 
keep a grand total and update it when we’ve gone hiking further.

The plus-equals operator also can be used for string concatenation, 
like so:

"""

