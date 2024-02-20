# ----------------------------------------------- #
#
# -- Total Score -- Python StudySpace --
#
# ----------------------------------------------- #

"""
A website that tracks basketball scores and stats is having trouble with its data. 
The first-half score and second-half score are stored in separate dictionaries, 
making it difficult for them to parse the overall score. 

They have asked you to 
help them write a program that merges the two dictionaries and another function 
that calculates the total score.

"""

# ------------------------------ #
# -- Assignment -- Practice --
# ------------------------------ #

"""
Complete the merge and total_score functions.

The merge function accepts two score dictionaries as input and returns a single 
merged dictionary that contains all of the keys and values from the input 
dictionaries.

The total_score function should take a single score dictionary as input and 
return the total score calculated from the values of that dictionary. Take a 
look at the test suite near the top of the file for the names of keys to expect. 

If no points were scored, the function should return 0.

Don't forget: you can always add print() statements to your code so that you can 
debug your code before submitting! Print out values of variables to see what's 
going on, and question your assumptions about what you think is happening.

"""

# ----------------------------- # 
# -- Debugging with Print Statements --
# ----------------------------- #

def total_score(score_dict):
    print(f"score_dict: {score_dict}")
    for key in score_dict:
        print(f"key: {key}")

"""
You would then run your code and manually inspect the output to see what's going 
on. You can always remove the print statements when you're done debugging if you 
want.

"""

# ----------------------------- #
# -- Buggy Code --
# ----------------------------- #

def merge(dict1, dict2):
    pass


def total_score(score_dict):
    pass

# ----------------------------- #
# -- Unit Test Cases --
# ----------------------------- #

from main import *

run_cases = [
    (
        {"first_quarter": 24, "second_quarter": 31},
        {"third_quarter": 29, "fourth_quarter": 40},
        124,
    ),
    (
        {"first_quarter": 12, "second_quarter": 2},
        {"third_quarter": 32, "fourth_quarter": 87},
        133,
    ),
]

submit_cases = run_cases + [
    (
        {"first_quarter": 25, "second_quarter": 2},
        {"third_quarter": 31, "fourth_quarter": 0},
        58,
    ),
    (
        {"first_quarter": 10, "second_quarter": 20},
        {"third_quarter": 30, "fourth_quarter": 40},
        100,
    ),
    (
        {"first_quarter": 15, "second_quarter": 25},
        {"third_quarter": 0, "fourth_quarter": 0},
        40,
    ),
    ({}, {}, 0),
    (
        {"first_quarter": 0, "second_quarter": 0},
        {"third_quarter": 0, "fourth_quarter": 0},
        0,
    ),
    (
        {"first_quarter": 100, "second_quarter": 100},
        {"third_quarter": 100, "fourth_quarter": 100},
        400,
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * first_half: {input1}")
    print(f" * second_half: {input2}")
    print(f"Expecting: {expected_output}")
    merged = merge(input1, input2)
    result = total_score(merged)
    print(f"Actual: {result}")
    if result == expected_output:
        if len(merged) == 4 or expected_output == 0:
            print("Pass")
            return True
        print("Dictionaries merged incorrectly")
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
# -- Worked on Code --
# ----------------------------- #

