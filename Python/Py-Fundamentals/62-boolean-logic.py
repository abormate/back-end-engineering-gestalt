# ------------------------------------- #
#
# -- Boolean Logic -- 
#
# ------------------------------------- #

"""
Boolean logic refers to logic dealing with boolean (True or False) values. For 
example,

Dogs must have four legs and weigh less than 100 kilograms. (Both conditions must 
be true)

"""

# ----------------------------- #
# -- Logical Operators Review --
# ----------------------------- #

"""
As we discussed earlier, the logical operators and and or can be used to perform 
boolean logic.

"""

# ---------------------------- #
# -- AND Review --
# ---------------------------- #

"""
The and operator returns True if both of the conditions on either side evaluates to 
True:

"""

def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100

"""
Let's go over how this function evaluates given the parameters num_legs=4 and 
weight=99:


return 4 == 4 and 99 < 100

return True and True

return True

"""

# Let's see what would happen with 3 and 98 instead:

"""
return 3 == 4 and 98 < 100

return False and True

return False

"""

# ------------------------ #
# -- OR Review
# ------------------------ #

"""
The or operator returns True if at least one of the conditions on either side 
evaluates to True:

"""

def is_car_cool(speed, is_electric):
    return speed > 200 or is_electric

# Let's use a non-electric car that can do 250:

"""
return 250 > 200 or False

return True or False

return True

"""

# ------------------------ #
# -- Assignment -- Practice
# ------------------------ #

"""
We need a way for our game to track whether a character's attack hits or misses.

Complete the does_attack_hit function. The function should return True if either of 
the following conditions are met:

-- The attack_roll is not a 1 and the attack roll is greater than or equal to 
     the armor_class
-- The attack roll is a 20


Otherwise, it should return False.


"""

# ----------------------- #
# -- Buggy Code --
# ----------------------- #

def does_attack_hit(attack_roll, armor_class):
    pass

# ---------------------- #
# -- Repaired Code --
# ---------------------- #

def does_attack_hit(attack_roll, armor_class):
    if (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20:
        return True
    else:
        return False