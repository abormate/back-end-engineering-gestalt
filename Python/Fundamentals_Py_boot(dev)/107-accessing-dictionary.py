# ---------------------------------------------- #
#
# -- Accessing Dictionary Values --
#
# ---------------------------------------------- #

"""
Dictionary elements must be accessible somehow in code, otherwise they wouldn't 
be very useful.

A value is retrieved from a dictionary by specifying its corresponding key in 
square brackets. The syntax looks similar to indexing into a list.

"""

car = {
    'make': 'tesla',
    'model': '3'
}

print(car['make'])
# Prints: tesla