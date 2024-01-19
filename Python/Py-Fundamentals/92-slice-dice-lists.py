# -------------------------------------------- #
#
# -- Slice Lists -- Python StudySpace --
#
# -------------------------------------------- #

"""
Python makes it easy to slice and dice lists to work only with the section you 
care about. One way to do this is to use the simple slicing operator, which is 
just a colon :.

With this operator, you can specify where to start and end the slice, and how to 
step through the original. List slicing returns a new list from the existing 
list.

The syntax is as follows:

my_list[ start : stop : step ]

"""

# For example --

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list

print(scores[1:5:2])
# Prints [70, 20]

