# ----------------------------------------- #
#
# -- Loops -- Python StudySpace --
#
# ----------------------------------------- #

# As a reminder, a loop in Python is written like...

for i in range(0, 10):
    print(i)

"""
In English, the code says:

Start with i equals 0. (i in range(0)
If i is not less than 10 (range(0, 10)), exit the loop.
Print i to the console. (print(i))
Add 1 to i. (range defaults to incrementing by 1)
Go back to step 2


The result is that the numbers 0-9 are logged to the console in order.

WHITESPACE MATTERS IN PYTHON!
The body of a for-loop must be indented; otherwise, you'll get a syntax error.

"""

# -------------------------- #
# -- Assignment -- Practice --
# -------------------------- #

"""
In the print_numbers function, write a for-loop from scratch that logs the 
numbers 0-199 to the console.

"""

# ------------------------- #
# -- Buggy Code --
# ------------------------- #

def print_numbers():
    # ?


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()

# --------------------------- #
# -- Repaired Code --
# --------------------------- #

def print_numbers():
    for i in range(0, 200):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()