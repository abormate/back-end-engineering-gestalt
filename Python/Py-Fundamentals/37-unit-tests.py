# ---------------------------------------------- #
#
# -- Unit Tests -- Python StudySpace --
#
# ---------------------------------------------- #

"""
Up until this point, all the coding lessons you've completed have been testing you based on console 
output (what's printed). For example, a lesson might expect your code (in conjunction with the code 
we provide) to print something like:

"""

Armor: 2
Health: 18

# If your code prints that exact output, you pass. If it doesn't, you fail.


# ------------------------------- #
# -- A new type of Lesson --
# ------------------------------- #

"""
Going forward, you'll encounter a new type of lesson: unit tests. A unit test is just an automated 
program that tests a small "unit" of code. Usually just a function or two.

These new unit-test-style lessons will test your code's functionality rather than its output. Our tests 
will call functions in your code with different arguments, and expect certain return values. If your 
code returns the correct values, you pass. If it doesn't, you fail.

There are two reasons for this change:


-- It's more realistic. In the real world, you'll be writing unit tests and running them against your code to make sure it works as expected.

-- You can run and debug your code with print statements, and leave those print statements in when you submit. Unlike the output-based lessons, you won't have to remove your print statements to pass.

"""

# ------------------------------ #
# -- Assignment -- Practice 
# ------------------------------ #

"""
Complete the level_up function. It accepts two integers as input:

-- level
-- xp_to_add

"""