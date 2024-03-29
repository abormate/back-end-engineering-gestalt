# ------------------------------------------------ #
#
# -- Duplicates -- Deduplication -- Python StudySpace --
#
# ------------------------------------------------ #

"""
----------
Scenario: 
----------

John is a data analyst, but he's bad with code. He has asked you for a script 
that can remove duplicates from some of his data sets.

"""

# -------------------------------------- #
# -- Assignment -- Practice --
# -------------------------------------- #

"""
Complete the remove_duplicates function. It accepts a list of strings and removes 
any duplicate values. It should utilize and return a set, not a list!

Bonus points if you can write the body of the function in a single line of code.

"""

# --------------------------------------- #
# -- Buggy Code Base --
# --------------------------------------- #

def remove_duplicates(lst):
    pass

# --------------------------------------- #
# -- Unit Test Cases --
# --------------------------------------- #

from main import *

run_cases = [
    (
        ["basketball", "football", "soccer", "baseball", "basketball"],
        {"basketball", "football", "soccer", "baseball"},
    ),
    (
        [
            "Age of Empires",
            "World of Warcraft",
            "Halo",
            "Call of Duty",
            "Age of Empires",
            "Magic the Gathering",
            "Halo",
        ],
        {
            "Age of Empires",
            "World of Warcraft",
            "Halo",
            "Call of Duty",
            "Magic the Gathering",
        },
    ),
]

submit_cases = run_cases + [
    (
        [
            "Lane",
            "Allan",
            "James",
            "Tiffany",
            "John",
            "Cameron",
            "Lane",
            "Allan",
            "James",
            "Tiffany",
            "John",
            "Cameron",
            "Chad",
            "Tj",
            "Tim",
            "Gertrude",
            "Stephanie",
        ],
        {
            "Lane",
            "Allan",
            "James",
            "Tiffany",
            "John",
            "Cameron",
            "Chad",
            "Tj",
            "Tim",
            "Gertrude",
            "Stephanie",
        },
    ),
    ([], set()),
    (["apple", "apple", "apple", "apple", "apple"], {"apple"}),
    (["a", "b", "c", "c", "b", "a"], {"a", "b", "c"}),
    (["123", "456", "789", "123", "456", "789"], {"123", "456", "789"}),
    (
        [
            "python",
            "java",
            "c++",
            "ruby",
            "python",
            "java",
            "c++",
            "ruby",
            "python",
            "java",
            "c++",
            "ruby",
            "python",
            "java",
            "c++",
            "ruby",
        ],
        {"python", "java", "c++", "ruby"},
    ),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input list: {input}")
    print(f"Expected set: {expected_output}")
    result = remove_duplicates(input)
    print(f"Actual set: {result}")
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

# ----------------------------------------- #
# -- Worked on Code --
# ----------------------------------------- #

def remove_duplicates(lst):
    return set(lst)