# -------------------------------------- #
#
# -- Double the String -- Python StudySpace --
#
# -------------------------------------- #

"""
An alien spaceship has landed on Earth! In an extremely realistic, and not 
completely fictional turn of events... the alien race speaks English, albeit a 
slightly modified version of English.

Our English: Hello there
Their English: HHeelllloo tthheerree

"""

# ---------------------------- #
# -- Assignment --
# ---------------------------- #

"""
Complete the double_string function. It takes a string as input and returns a 
"doubled" version, including spaces!

Example output

sentence = "hi im an alien"
print(double_string(sentence)) # "hhii  iimm  aann  aalliieenn"


"""

# ---------
# -- TIP --
# ---------

# You can iterate over a string as if it were a list of individual characters.

# ------------------------------ #
# -- Buggy Code --
# ------------------------------ #

def double_string(string):
    pass

# ------------------------------ #
# -- Unit Test Cases --
# ------------------------------ #

from main import *

run_cases = [
    ("Hello there", "HHeelllloo  tthheerree"),
    ("General Kenobi", "GGeenneerraall  KKeennoobbii"),
]

submit_cases = run_cases + [
    ("I am an alien", "II  aamm  aann  aalliieenn"),
    ("Python is fun", "PPyytthhoonn  iiss  ffuunn"),
    ("I love coding", "II  lloovvee  ccooddiinngg"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = double_string(input1)
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

# ------------------------------ #
# -- Worked on Code --
# ------------------------------ #

