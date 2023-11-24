# ------------------------------------- #
#
# -- Number Syntax -- Python StudySpace --
#
# ------------------------------------- #

"""
Challenge Exercise

You've been working with a biologist who is researching the mating behaviors of 
fruit bats. They've added some calls to the main function that contain invalid 
syntax.

Fix the biologist's syntax error. Use the proper delimiter so that the numbers 
are still easy to parse visually.


The numbers should be:

8 million and 3 million
10 million and 4.5 million

"""

# -------------------------- #
# -- Buggy Code --
# -------------------------- #

def main():
    test(8,000,000, 3,000,000)
    test(10,000,000, 4,500,000)


# Don't edit below this line


def calculate_male_ratio(num_fruit_bats, num_male_bats):
    return num_male_bats / num_fruit_bats


def test(num_fruit_bats, num_male_bats):
    ratio = calculate_male_ratio(num_fruit_bats, num_male_bats)
    print(f"{ratio * 100}% of fruit bats are male")
    print("=====================================")


main()

# -------------------------- #
# -- Repaired Code --
# -------------------------- #

def main():
    test(8_000_000, 3_000_000)
    test(10_000_000, 4_500_000)


# Don't edit below this line


def calculate_male_ratio(num_fruit_bats, num_male_bats):
    return num_male_bats / num_fruit_bats


def test(num_fruit_bats, num_male_bats):
    ratio = calculate_male_ratio(num_fruit_bats, num_male_bats)
    print(f"{ratio * 100}% of fruit bats are male")
    print("=====================================")


main()

