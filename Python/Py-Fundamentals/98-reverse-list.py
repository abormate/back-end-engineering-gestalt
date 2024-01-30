# ---------------------------------------- #
#
# -- Reverse List -- Python StudySpace --
#
# ---------------------------------------- #

"""
Some of our players would like to view their inventories in reverse order.

Let's write a function that takes a list as an input and returns a new list 
except all the items are in reverse order.

For example:

[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

"""

# ------- #
# TIP! 
# ------- #

"""
The Python range function is very useful when working with lists. Alternately, 
you may want to use list slicing.

-- Where should you start your loop from?

-- Where should you end your loop?

-- What should the step be? In other words, how should you increment i in each 
iteration of the loop?


"""

# ---------------------------- #
# -- Buggy Code --
# ---------------------------- #

def reverse_array(items):
    pass

# ---------------------------- #
# -- Unit Test --
# ---------------------------- #

from main import *

run_cases = [
    (
        ["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"],
        ["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"],
    ),
    ([1, 2, 300, 4, 5], [5, 4, 300, 2, 1]),
]

submit_cases = run_cases + [
    ([], []),
    (["a"], ["a"]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (
        ["apple", "banana", "cherry", "date", "elderberry"],
        ["elderberry", "date", "cherry", "banana", "apple"],
    ),
    (["hello", "world"], ["world", "hello"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input array: {input}")
    print(f"Expected reversed array: {expected_output}")
    result = reverse_array(input)
    print(f"Actual reversed array: {result}")
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

# ---------------------------- #
# -- Worked on Code --
# ---------------------------- #

