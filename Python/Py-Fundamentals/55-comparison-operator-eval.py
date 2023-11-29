# ----------------------------------------- #
#
# -- Comparison Operator Evaluations --
#
# ----------------------------------------- #

"""
When a comparison happens, the result of the comparison is just a boolean value, 
it's either True or False.

Take the following two examples:

"""

is_bigger = 5 > 4

is_bigger = True

"""
In both of the above cases, we're creating a Boolean variable called is_bigger 
with a value of True.

Because 5 is greater than 4, is_bigger is assigned the value of True.

"""

# ----------------------- #
# -- Assignment -- Practice --
# ----------------------- #

"""
Use comparison operators to calculate and return the following values:

bob_as_tall_as_elon
sara_as_tall_as_elon
jill_as_tall_as_sara


Note: We are trying to calculate if these individuals are the exact same height.

"""

# --------------------- #
# -- Buggy Code --
# --------------------- #

def compare_heights(elon_height, sara_height, jill_height, bob_height):
    pass

# --------------------- #
# -- Repaired Code --
# --------------------- #

def compare_heights(elon_height, sara_height, jill_height, bob_height):
    bob_as_tall_as_elon = bob_height == elon_height
    sara_as_tall_as_elon = sara_height == elon_height
    jill_as_tall_as_sara = jill_height == sara_height
    return bob_as_tall_as_elon, sara_as_tall_as_elon, jill_as_tall_as_sara