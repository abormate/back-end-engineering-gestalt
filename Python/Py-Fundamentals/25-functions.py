# -------------------------------------- #
#
# -- Functions -- Python StudySpace --
#
# -------------------------------------- #

"""
Functions allow us to reuse and organize code. For example, let's pretend we need to calculate the area of a circle. We can use the formula area = pi * r^2, or in code:

"""

r = 5
area = 3.14 * r * r

"""
This works great! The problem arises when multiple places in our code need to get the area of a circle.

"""

r = 5
area1 = 3.14 * r * r

r2 = 7
area2 = 3.14 * r2 * r2

r3 = 11
area3 = 3.14 * r3 * r3


"""
We want to use the same code, why repeat the work?

Let's declare a new function called area_of_circle. Notice that the def keyword is written before the function name, and tells the computer that we're defining a new function.

"""

