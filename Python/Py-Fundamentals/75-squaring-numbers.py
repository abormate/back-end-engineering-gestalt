# ---------------------------------------- #
#
# -- Squaring Numbers -- Python StudySpace --
#
# ---------------------------------------- # 

"""
John is finishing some math homework and needs to calculate the square of some 
numbers. However, he's getting tired of entering each of them into a calculator 
individually.

The square of a number is just the number multiplied by itself.

"""

# ---------------------------- #
# -- Assignment -- Practice --
# ---------------------------- #

"""
In the calculate_squares function, write a loop that calculates and prints the 
squares of the numbers from the start parameter up to the given end parameter.

Use the following format to print each line:

"""

# NUM squared = SQUARE

"""
Where NUM is the number, and SQUARE is its square.

For example, the first iteration of the loop in calculate_squares(100, 110) 
should print:

"""

# 100 squared = 10000

# Note that the end is exclusive and will not be included in the printed output.

# ---------------------------- #
# -- Buggy Old Code --
# ---------------------------- #

'''
def calculate_squares(start, end):
    # ?


# Don't edit below this line


     def test(start, end):
          print(f"Calculating squares from {start} to {end - 1}:")
          calculate_squares(start, end)
          print("=====================================")


def main():
    test(100, 105)
    test(1, 3)
    test(11, 14)


main()
'''

# ----------------------------- #
# -- Repaired Code --
# ----------------------------- #

def calculate_squares(start, end):
    square = 0
    for i in range(start, end):
        square = i*i
        print(f"{i} squared = {square}")


# Don't edit below this line


def test(start, end):
    print(f"Calculating squares from {start} to {end - 1}:")
    calculate_squares(start, end)
    print("=====================================")


def main():
    test(100, 105)
    test(1, 3)
    test(11, 14)


main()