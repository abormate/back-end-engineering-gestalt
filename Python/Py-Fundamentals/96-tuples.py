# ----------------------------------- #
#
# -- Tuples -- Python StudySpace --
#
# ----------------------------------- #

"""
Tuples are collections of data that are ordered and unchangeable. You can think 
of a tuple as a List with a fixed size. Tuples are created with round brackets:

"""

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True

"""
While it's typically considered bad practice to store items of different types in 
a List it's not a problem with Tuples. Because they have a fixed size, it's easy
to keep track of which indexes store which types of data.

Tuples are often used to store very small groups (like 2 or 3 items) of data. For 
example, you might use a tuple to store a dog's name and age.

"""