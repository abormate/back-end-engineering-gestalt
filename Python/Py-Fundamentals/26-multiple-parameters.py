# ----------------------------------------- #
#
# -- Multiple Parameters -- Python StudySpace
#
# ----------------------------------------- #

"""
Functions can have multiple parameters (which is just a fancy name for "inputs"). For example, this subtract function accepts 2 values as parameters, a and b:

"""

def subtract(a, b):
    return a - b


result = subtract(5, 3)
print(result)
# 2

# ------------------------- #
# -- Assignment -- Practice --
# ------------------------- #

"""
We need to be able to calculate the total damage from an attack involving 3 different enemies. Complete the calculate_damage function that takes three numbers as its 
parameters and returns the result of adding them all together.

"""

# ------------------------ #
# -- Buggy Code --
# ------------------------ #

def calculate_damage(enemy_one_dmg, enemy_two_dmg, enemy_three_dmg):
    # ?


# Don't touch below this line

print(f"You dealt {calculate_damage(2, 3, 4)} points of damage!")
print(f"You dealt {calculate_damage(-1, 4, 3)} points of damage!")
print(f"You dealt {calculate_damage(3, 2, 4)} points of damage!")
print(f"You dealt {calculate_damage(1, 4, 2)} points of damage!")


# ---------------------- #
# -- Fixed Code --
# ---------------------- #

def calculate_damage(enemy_one_dmg, enemy_two_dmg, enemy_three_dmg):
    return enemy_one_dmg + enemy_two_dmg + enemy_three_dmg


# Don't touch below this line

print(f"You dealt {calculate_damage(2, 3, 4)} points of damage!")
print(f"You dealt {calculate_damage(-1, 4, 3)} points of damage!")
print(f"You dealt {calculate_damage(3, 2, 4)} points of damage!")
print(f"You dealt {calculate_damage(1, 4, 2)} points of damage!")

