# ------------------------------------------ #
#
# -- Find an Item in a List --
#
# ------------------------------------------ #

# Example of "no-index" or "no-range" syntax:

"""
for fruit in fruits:
    print(fruit)
"""

# --------------------------- #
# -- Assignment -- Practice --
# --------------------------- #
    
"""
We need to check if a player has a specific item in their inventory. In the 
contains_leather_scraps function, use the no-index syntax to iterate over each 
item in items. If you find an item called Leather Scraps, set the found variable 
to True.

"""

# --------------------------- #
# -- Buggy Code --
# --------------------------- #

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    # ?

    # don't touch below this line

    return found

# --------------------------- #
# -- Unit Tester --
# --------------------------- #

from main import *

run_cases = [
    (["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"], True),
    (["Potion", "Shortsword", "Buckler", "Iron Mace"], False),
]

submit_cases = run_cases + [
    ([], False),
    (["Leather Scraps"], True),
    (["Potion", "Leather Scraps", "Leather Scraps"], True),
    (["Potion", "Healing Potion"], False),
    (["Leather scraps"], False),
    (["Leather", "Scraps"], False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = contains_leather_scraps(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

# --------------------------- #
# -- Work Code --
# --------------------------- #

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather Scraps":
            found = True

    # don't touch below this line

    return found