# ---------------------------------- #
#
# -- List Length -- Python StudySpace --
#
# ---------------------------------- #

# The length of a List can be calculated using the len() function.

fruits = ["apple", "banana", "pear"]
length = len(fruits)
# Prints: 3

"""
The length of the list is equal to the number of items present. Don't be fooled 
by the fact that the length is not equal to the index of the last element, in 
fact, it will always be one greater.

"""

# ------------------------ #
# -- Assignment -- Practice --
# ------------------------ #

"""
Some of our player's inventories are huge, so looking through the entire list is 
cumbersome. Let's find an easy way for us to get the index of the last item in 
their inventory.

Complete the get_last_index function so that it returns the length of the 
inventory list minus 1.

"""

# ------------------------ #
# -- Buggy Code --
# ------------------------ #

def get_last_index(lst):
    pass

# ------------------------ #
# -- Unit Test --
# ------------------------ #

from main import *

run_cases = [
    (["Potion"], 0),
    (["Potion", "Iron Breastplate"], 1),
    (["Potion", "Iron Breastplate", "Bread", "Longsword"], 3),
]

submit_cases = run_cases + [
    ([], -1),
    (["Single item"], 0),
    (["Shield", "Sword", "Bow", "Arrows", "Health Potion"], 4),
    (["Shield", "Sword", "Bow"], 2),
    (["Shield", "Sword"], 1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_last_index(input1)
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

# -------------------------- #
# -- Repaired Code --
# -------------------------- #

def get_last_index(lst):
    return len(lst) - 1