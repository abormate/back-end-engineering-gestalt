# ----------------------------------------------- #
#
# -- Unordered Sets -- Python StudySpace --
#
# ----------------------------------------------- #

"""
Sets are like Lists, but they are unordered and they guarantee uniqueness. Only 
ONE of each value can be in a set.

"""

fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

# -------------------------------- #
# -- Add Values --
# -------------------------------- #

fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

# Note: No error will be raised if you add an item already in the set.

# ------------------------------- #
# -- Empty Set --
# ------------------------------- #

"""
Because the empty bracket {} syntax creates an empty dictionary, to create an 
empty set, you need to use the set() function.

"""

fruits = set()

# ------------------------------- #
# -- Assignment -- Practice --
# ------------------------------- #

"""
Complete the remove_duplicates function. It should take a list of spells that a 
player has learned and return a new List where there is at most one of each title. You can accomplish this by creating a set, adding all the spells to it, then iterating over the set and adding all the spells back into a List and returning the list.

It makes no sense to learn a spell twice! Once it's learned, it's learned 
forever.

"""

# ------------------------------- #
# -- Buggy Code --
# ------------------------------- #

def remove_duplicates(spells):
    pass

# ------------------------------- #
# -- Unit Test Cases --
# ------------------------------- #

from main import *

run_cases = [
    (
        [
            "fireball",
            "eldrich blast",
            "fireball",
            "eldrich blast",
            "water gun",
            "eldrich blast",
            "water gun",
            "water gun",
            "fireball",
            "fireball",
            "sunburst",
            "fireball",
            "fireball",
        ],
        ["eldrich blast", "fireball", "sunburst", "water gun"],
    )
]

submit_cases = run_cases + [
    (["fireball", "fireball", "fireball"], ["fireball"]),
    (
        ["fireball", "eldrich blast", "water gun", "sunburst"],
        ["eldrich blast", "fireball", "sunburst", "water gun"],
    ),
    (["water gun", "water gun", "water gun"], ["water gun"]),
    (["sunburst", "sunburst", "sunburst"], ["sunburst"]),
    ([], []),
    (["eldrich blast", "eldrich blast", "eldrich blast"], ["eldrich blast"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * spells: {input}")
    print(f"Expecting: {expected_output}")
    result = remove_duplicates(input)
    if isinstance(result, list):
        result.sort()
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

# ------------------------------------- #
# -- Worked on Code --
# ------------------------------------- #

def remove_duplicates(spells):
    spells_set = set()
    for spell in spells:
        spells_set.add(spell)
    deduped_spells = []
    for deduped_spell in spells_set:
        deduped_spells.append(deduped_spell)
    return deduped_spells