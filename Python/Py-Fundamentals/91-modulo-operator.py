# ---------------------------------------- #
#
# -- Modulo Operator -- Python StudySpace --
#
# ---------------------------------------- #

"""
For example, 7 modulo 2 would be 1, because 2 can be multiplied evenly into 7 at 
most 3 times:

Then there is 1 remaining to get from 6 to 7.

The modulo operator is the percent sign: %. It's important to recognize modulo is
not a percentage though! That's just the symbol we're using.

"""

remainder = 8 % 3
# remainder = 2

# ! Important ! -- An odd number is a number that when divided by 2, 
#               -- the remainder is not 0.


# ----------------------------- #
# -- Assignment --
# ----------------------------- #

"""
Inside the loop in the get_odd_numbers function, use the modulo operator to check 
if each number, i, is odd. If a number is odd, append it to the odd_numbers list.

"""

# ----------------------------- #
# -- Buggy Code --
# ----------------------------- #

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        pass

    # don't touch below this line

    return odd_numbers

# ----------------------------- #
# -- Unit Test --
# ----------------------------- #

