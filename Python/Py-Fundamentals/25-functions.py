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

def area_of_circle(r):
    return 3.14 * r * r


"""
The area_of_circle function takes one input (which can also be called a "parameter" or "argument") and returns a single output. We give our function the radius of a circle 
and we get back the area of that circle!

To use or "call" the function we can pass in any number as the input, and capture the output into a new variable:

"""

radius = 5
area = area_of_circle(radius)
print(area)
# 78.5

"""
Let's talk through this code example step by step.

The radius variable is created with a value of 5.
The area_of_circle function is called with a single argument: radius
The area_of_circle function is executed, with r being equal to 5
The result of 3.14 * r * r is returned from area_of_circle, which... bangs on calculator... happens to be 78.5
The area_of_circle(radius) evaluates to the returned value of 78.5
The area variable is created and set to a value of 78.5
The built-in print function prints the value of area to the console, which is 78.5

"""

# ---------------------------- #
# -- Assignment -- Practice --
# ---------------------------- #

