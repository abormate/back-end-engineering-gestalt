# ------------------------------------------ #
#
# -- Experience Points -- Python StudySpace --
#
# ------------------------------------------ #

"""
You've been hired by a game studio to work on their latest role-playing game, in 
this game adventurers need experience points (XP) to level up and become 
stronger. 

You've been tasked with creating a function to calculate the total amount of XP 
needed for a player to reach a specific level.

Each character starts with 0 XP at level 1. To reach the next level, they need 5 
more XP than the last level required. So level 2 requires just 5 XP, while level 
3 requires 10.

"""

# --------------------------- #
# -- Challenge --
# --------------------------- #

"""
Complete the calculate_experience_points function.

The calculate_experience_points function takes a single parameter named level. 
Determine how many XP are required to get to the specified level from level 1 
with 0 XP.

"""

    #   0xp -> lvl 1 (O * 5)
    #  +5xp -> lvl 2 (1 * 5)
    # +10xp -> lvl 3 (2 * 5)
    # +15xp -> lvl 4 (3 * 5)
    #------
    #  30xp

    # calculate_experience_points(4)
    # returns 30

# ------------------------- #
# -- Tip --
# ------------------------- #

"""
The formula:

(The XP needed for all previous levels) + (the current level multiplied by 5)

Remember that we are only calculating the XP needed to reach the level that was 
passed in. That means we need to calculate the XP for all levels up to, but not 
including, the given level parameter.


"""

# ----------------------- #
# -- Buggy Code --
# ----------------------- #

def calculate_experience_points(level):
    pass

# ----------------------- #
# -- Unit Test Cases --
# ----------------------- #

from main import *

run_cases = [
    (2, 5),
    (3, 15),
    (4, 30),
]

submit_cases = run_cases + [
    (1, 0),
    (5, 50),
    (7, 105),
    (10, 225),
    (15, 525),
    (20, 950),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = calculate_experience_points(input1)
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

# ------------------------ #
# -- Repaired Code --
# ------------------------ #

def calculate_experience_points(level):
    exp = 0
    for i in range(1, level):
        exp += i * 5

    return exp