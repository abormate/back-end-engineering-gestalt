# -------------------------------------- #
#
# -- Evens and Odds -- Python StudySpace --
#
# -------------------------------------- #

"""
You've been asked to write a program that will calculate how many odd and even 
numbers exist in a list.

"""

# ---------------------------- #
# -- Assignment --
# ---------------------------- #

"""
Write the get_odds_and_evens function to loop through the numbers list and check 
if each number in the list is either odd or even.

Increment the num_evens counter if even, and the num_odds counter if it's odd. 
Lastly, return the two values num_odds and num_evens in that order.

----------
!! TIP !!
----------

Remember, you can check if a number is even by using the modulo operator (%).

"""

# ---------------------------- #
# -- Buggy Code --
# ---------------------------- #

def get_odds_and_evens(numbers):
    num_evens = 0
    num_odds = 0

    # Don't touch above this line

    pass

# --------------------------- #
# -- Unit Tester --
# --------------------------- #

from main import *

run_cases = [
    ([1, 7, 2, 5, 3, 4], (4, 2)),
    ([0, 99, 2, 33, 61, 44, 9, 10, 12, 240, 35, 9082, 1234], (5, 8)),
]

submit_cases = run_cases + [
    ([], (0, 0)),
    ([1, 3, 5, 7, 9], (5, 0)),
    ([2, 4, 6, 8, 10], (0, 5)),
    ([1], (1, 0)),
    ([2], (0, 1)),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (5, 5)),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_odds_and_evens(input1)
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

# ------------------------------- #
# -- Worked on Code --
# ------------------------------- #

def get_odds_and_evens(numbers):
    num_evens = 0
    num_odds = 0

    # Don't touch above this line

    pass
    pass

