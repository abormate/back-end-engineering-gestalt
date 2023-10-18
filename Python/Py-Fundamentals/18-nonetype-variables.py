# -------------------------------------- #
#
# -- Nonetype Variables -- Python StudySpace --
#
# -------------------------------------- #

"""
Not all variables have a value. We can declare an "empty" variable by setting it to None.

"""

empty = None


"""
The value of empty in this instance is None until we use the assignment operator, =, to give it a value.

"""

# ------------------------- #
# -- None is not a Specific String --
# ------------------------- #

# Note that the None type is not the same as a string with a value of "None":

my_none = None # this is a None-type
my_none = "None" # this is a string


# ------------------------- #
# -- Assignment -- Practice --
# ------------------------- #

# Declare a variable named enemy and set it to None. Don't change the print() function.

# ------------------------ #
# -- Old buggy code --
# ------------------------ #

# create the empty "enemy" variable here


# don't touch below this line
# print(enemy is None)


# ----------------------- #
# -- New fixed code --
# ----------------------- #

enemy = None

print(enemy is None)

"""
As we mentioned in the last exercise, the None keyword is used to define a null variable or object. In Python, the None keyword is an object 
(which we'll cover later), and it is a data type of the class NoneType.

"""

