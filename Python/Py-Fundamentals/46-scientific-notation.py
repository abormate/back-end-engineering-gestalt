# -------------------------------------------- #
#
# -- Scientific Notation -- Python StudySpace
#
# -------------------------------------------- #

"""
As we covered earlier, a float is a positive or negative number with a fractional 
part.

You can add the letter e or E followed by a positive or negative integer to 
specify that you're using scientific notation.

"""

print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

"""
If you're not familiar with scientific notation, it's a way of expressing numbers 
that are too large or too small to conveniently write normally.

In a nutshell, the number following the e specifies how many places to move the 
decimal to the right for a positive number, or to the left for a negative number.

"""

# --------------------------- #
# Underscores for Readability
# --------------------------- #

"""
Python also allows you to represent large numbers in the decimal format using 
underscores instead of commas to make it easier to read.

"""

num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

# ------------------------- #
# Assignment -- Practice
# ------------------------- #

"""
Due to the constraints of our app's server, we have the maximum number of players 
we can have on a single "Fantasy Quest" server.

Complete the max_players_on_server function. It should return 3 values:

The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
The max players on a "medium" server: 10,240,000,000,000,000,000
The max players on a "large" server: 102,400,000,000,000,000,000
Use scientific notation to represent these numbers.

"""

