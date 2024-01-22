# ------------------------------------------------ #
#
# -- List Operations -- Contains -- Python StudySpace --
#
# ------------------------------------------------ #

"""
Checking whether a value exists in a list is also really easy in Python, just use 
the in keyword.

"""

fruits = ["apple", "orange", "banana"]
print("apple" in fruits)
# Prints: True

# ----------------------------------- #
# -- Assignment -- Practice --
# ----------------------------------- #

"""
Our players have requested an in-game feature that will allow them to type in a 
weapon name to check if it's in the list of top weapons in the realm.

Complete the is_top_weapon function. It should return True if the weapon is in 
the top_weapons list, otherwise it should return False.

"""

# ----------------------------------- #
# -- Buggy Code --
# ----------------------------------- #

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line

    pass

# ---------------------------------- #
# -- Unit Test --
# ---------------------------------- #

