# ------------------------------------- #
#
# -- Binary -- 
#
# ------------------------------------- #

"""
You've been assigned to write some tests for the Python interpreter itself! Python 
has built-in functionality to parse strings of 1's and 0's as binary numbers.

"""

# ---------------------- #
# -- Challenge --
# ---------------------- #

"""
Complete the body_parts function. It takes binary strings as input and returns 
them as integers. Each integer is the numerical value of the string when 
interpreted as binary.

For example:

"""
body_parts = []
heads, arms, fingers = body_parts("100", "101", "110")
print(heads)
# 4
print(arms)
# 5
print(fingers)
# 6

# TIP
"""
The built-in int function can convert a binary string to an integer. It takes a 
second argument that specifies the base of the number (binary is base 2). 

For example:

"""

# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)


# -------------------------------- #
# -- Assignment -- Practice -- 
# -------------------------------- #

def body_parts(num_heads, num_arms, num_fingers):
    pass