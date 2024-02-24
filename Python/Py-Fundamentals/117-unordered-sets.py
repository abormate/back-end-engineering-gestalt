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