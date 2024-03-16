# ------------------------------------------- #
#
# -- Differences -- Python StudySpace --
#
# ------------------------------------------- #

"""
Your local gym recently bought out another gym, and they're trying to merge their 
customer data. You've been given 2 lists of customer IDs (numbers) and are trying 
to figure out which customers from the first gym are not also members of the 
second gym. Luckily, the IDs from the 2 gyms match up because they used the same 
back-end servers.


"""

# --------------------------- #
# -- Activity -- Practice --
# --------------------------- #

"""
Complete the find_missing_ids function. It accepts two lists as input, and 
returns a new list of all the ids present in the first list but not the second.

Keep in mind, there may be duplicate ids in these lists, the gym workers aren't 
exactly concerned about data integrity. Make sure to remove any duplicates.

"""

# --------- #
# -- Tip --
# --------- #

"""
You can convert a List to a Set using the set() function.
You can convert a Set to a List using the list() function.
You can subtract the elements in one Set from another Set using the - operator.

"""

# -------------------------- #
# -- Buggy Code --
# -------------------------- #

def find_missing_ids(first_ids, second_ids):
    pass

# -------------------------- #
# -- Unit Test Cases --
# -------------------------- #

from main import *

run_cases = [
    ([1, 1, 1, 2, 2, 2, 3], [1, 2], [3]),
    ([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8], [9, 10]),
]

submit_cases = run_cases + [
    ([], [], []),
    ([1, 1, 1], [], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], []),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3], []),
    ([1, 2, 3, 4, 5], [1, 2, 3], [4, 5]),
    ([1, 2, 3, 4, 5], [1, 3, 5], [2, 4]),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: first_ids = {input1}, second_ids = {input2}")
    print(f"Expecting: {expected_output}")
    result = find_missing_ids(input1, input2)
    if isinstance(result, list):
        result = sorted(result)
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

# ---------------------------------- #
# -- Code Fix --
# ---------------------------------- #

def find_missing_ids(first_ids, second_ids):
    s1 = set(first_ids)
    s2 = set(second_ids)
    return list(s1 - s2)
