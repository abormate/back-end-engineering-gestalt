# --------------------------------------- #
#
# -- Plus Equals -- Python StudySpace --
#
# --------------------------------------- #

"""
Python makes reassignment easy when doing math. In JavaScript or Go you might be 
familiar with the ++ syntax for incrementing a number variable. In Python, we use 
the += operator instead.

"""

star_rating = 4
star_rating += 1
# star_rating is now 5

# --------------------------- #
# -- Other Operations --
# --------------------------- #

# The following operations work similarly

star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2

# ------------------------------- #
# -- Assignment -- Practice --
# ------------------------------- #

"""
Complete the get_hurt function. It should use the -= operator to subtract damage 
from current_health and then return the new current_health.

"""

# TIP
"""
You cannot use -= in a return statement. Set the variable first, and then return 
it after!

"""

# ------------------------------- #
# -- Buggy Code --
# ------------------------------- #

def get_hurt(current_health, damage):
    pass

# ------------------------------- #
# -- Unit Test --
# ------------------------------- #

from main import *

run_cases = [
    (1000, 100, 900),
    (900, 60, 840),
]

submit_cases = run_cases + [
    (840, 10, 830),
    (830, 3, 827),
    (0, 0, 0),
    (1, 1, 0),
    (100, 2, 98),
    (2500, 3, 2497),
]


def test(current_health, damage, expected_output):
    print("---------------------------------")
    print(f"Inputs: {current_health}, {damage}")
    print(f"Expecting: {expected_output}")
    result = get_hurt(current_health, damage)
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


# ----------------------------------- #
# -- Repaired Code --
# ----------------------------------- #

def get_hurt(current_health, damage):
    current_health -= damage
    return current_health