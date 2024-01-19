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

"""
The above reads as "give me a slice of the scores list from index 1, up to but 
not including 5, skipping every 2nd value. All of the sections are optional.

"""

# --------------------------- #
# -- Omitting Sections --
# --------------------------- #

"""
You can also omit various sections ("start", "stop", or "step"). For example, 
numbers[:3] means "get all items from the start up to (but not including) index 3". 
numbers[3:] means "get all items from index 3 to the end".

"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

# -------------------------- #
# -- Only the Step section --
# -------------------------- #

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]


