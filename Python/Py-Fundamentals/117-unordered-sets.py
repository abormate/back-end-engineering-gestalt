# ----------------------------------------------- #
#
# -- Unordered Sets -- Python StudySpace --
#
# ----------------------------------------------- #

"""
Sets are like Lists, but they are unordered and they guarantee uniqueness. Only 
ONE of each value can be in a set.

"""

fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

# -------------------------------- #
# -- Add Values --
# -------------------------------- #

fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

# Note: No error will be raised if you add an item already in the set.

# ------------------------------- #
# -- Empty Set --
# ------------------------------- #

"""
Because the empty bracket {} syntax creates an empty dictionary, to create an 
empty set, you need to use the set() function.

"""

fruits = set()