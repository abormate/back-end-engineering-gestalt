# -------------------------------------- #
#
# -- Test Scores -- Python StudySpace --
#
# -------------------------------------- #

"""
Your teacher has been manually grading tests by hand and it has been taking up 
all of her free time. 

She has asked you to write a program that compares an answer key to a student's 
multiple-choice answers and calculates the percentage of questions they got right.

"""

# -------------------------- #
# -- Assignment --
# -------------------------- #

""" 
Finish the get_test_scores function by looping over the answer_sheet and 
student_answers lists. Calculate and return the student's score.

For example, if these were the lists:

"""

answer_sheet = ["A", "A", "C", "D"]
student_answers = ["A", "B", "C", "D"]

"""
Then the percentage would be 75.00. The percentage should be a float, 
not an integer.

"""

# -------------------------- #
# -- Buggy Code --
# -------------------------- #

def get_test_score(answer_sheet, student_answers):
    pass

# -------------------------- #
# -- Unit Test Cases --
# -------------------------- #

from main import *

run_cases = [
    (
        ["A", "A", "C", "D", "D", "B", "C", "D"],
        ["A", "B", "C", "A", "D", "B", "C", "D"],
        (75.0),
    ),
    (
        ["A", "B", "C", "D", "D", "B", "C"],
        ["A", "B", "C", "D", "D", "B", "C"],
        (100.00),
    ),
]

submit_cases = run_cases + [
    (["A", "B", "C", "D", "D", "B", "C"], ["B", "A", "B", "A", "A", "C", "A"], (0.00)),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nanswer_sheet: {input1}\nstudent_answers: {input2}")
    print(f"Expecting: {expected_output}")
    result = get_test_score(input1, input2)
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
# -- Worked on Code --
# ------------------------ #

def get_test_score(answer_sheet, student_answers):
    score = 0
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i]:
            score += 1
    percentage = score / len(answer_sheet) * 100
    return percentage