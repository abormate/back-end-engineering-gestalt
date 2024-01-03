# ------------------------------------- #
#
# -- Prime Numbers -- Prime 
#
# ------------------------------------- #

"""
A math student is working on a project and needs an easy way to determine whether 
or not a number is prime. She asked you to write a program to help her.

"""

# -------------------------- #
# -- Assignment -- Practice --
# -------------------------- #

"""
Write a function that takes a single number as input and returns True if it is a 
prime number or False if it is not.

WHAT IS A PRIME NUMBER?
A prime number is a positive integer, greater than 1, that is only divisible by 
itself and 1. For example, 2, 3, 5, and 7 are all prime numbers, but 1, 4, 6, 8, 
and 9 are not.

"""

# ------------------------ #
# -- Tip --
# ------------------------ #

"""
0 and 1 are not prime numbers! And don't forget to catch all negative numbers!

We'll talk more about it next chapter, but you can use the modulo operator % to 
find a remainder. For example, 7 modulo 2 would be 1, because 2 can be multiplied 
evenly into 7 at most 3 times.

"""

remainder = 8 % 3
# remainder = 2

remainder = 9 % 3
# remainder = 0

# ------------------------ #
# -- Unit Test Cases --
# ------------------------ #

from main import *

run_cases = [
    (7, True),
    (-7, False),
    (9, False),
    (23, True),
]

submit_cases = run_cases + [
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (4, False),
    (31, True),
    (100, False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input number: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_prime(input1)
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

# ----------------------------- #
# -- Code --
# ----------------------------- #

