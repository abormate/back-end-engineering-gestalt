# ---------------------------------------- #
#
# -- Modulo Operator -- Python StudySpace --
#
# ---------------------------------------- #

"""
For example, 7 modulo 2 would be 1, because 2 can be multiplied evenly into 7 at 
most 3 times:

Then there is 1 remaining to get from 6 to 7.

The modulo operator is the percent sign: %. It's important to recognize modulo is
not a percentage though! That's just the symbol we're using.

"""

remainder = 8 % 3
# remainder = 2

# ! Important ! -- An odd number is a number that when divided by 2, 
#               -- the remainder is not 0.


# ----------------------------- #
# -- Assignment --
# ----------------------------- #

"""
Inside the loop in the get_odd_numbers function, use the modulo operator to check 
if each number, i, is odd. If a number is odd, append it to the odd_numbers list.

"""

# ----------------------------- #
# -- Buggy Code --
# ----------------------------- #

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        pass

    # don't touch below this line

    return odd_numbers

# ----------------------------- #
# -- Unit Test --
# ----------------------------- #

from main import *

run_cases = [(10, [1, 3, 5, 7, 9]), (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])]

submit_cases = run_cases + [
    (0, []),
    (1, []),
    (2, [1]),
    (300, [i for i in range(1, 300, 2)]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_odd_numbers(input1)
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
# -- Worked on Code --
# --------------------------- #

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers