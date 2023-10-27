# -------------------------------------- #
#
# -- Order of Functions -- Python StudySpace
#
# -------------------------------------- #

# All functions must be defined before they're used.

"""
You might think this would make structuring Python code difficult because the order in which the functions are declared can quickly become so dependent on each other that 
writing anything becomes impossible.

As it turns out, most Python developers solve this problem by simply defining all the functions in their program first, then finally calling the entrypoint function last. 
If you do that, then the order of the function definitions doesn't matter. The entrypoint function is conventionally called "main".

"""

def main():
    func2()

def func2():
    func3()

def func3():
    print("I'm function 3")

# call entrypoint last
main()

# ------------------------- #
# -- Assignment -- Practice
# ------------------------- #

# Write a function called to_celsius that converts a temperature in Fahrenheit to Celsius