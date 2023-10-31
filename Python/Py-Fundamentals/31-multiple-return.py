# -------------------------------------- #
#
# -- Multiple Return Values --
# 
# -------------------------------------- #

"""
In Python, we can return more than one value from a function. All we need to do is separate each value we are returning by a comma, and when we call the function, 
we need to capture all the returned values in individual variables.

"""

# returns email, age, and status of the user
def get_user():
    return "name@domain.com", 21, "active"

# sets email, age, and status to values returned from get_user() function
email, age, status = get_user()
print(email, age, status)
# name@domain.com 21 active

# -------------------------- #
# Assignment -- Practice --
# -------------------------- #

"""
Complete the become_warrior function. It accepts 3 inputs:

first_name: A string
last_name: A string
power: An integer


It should return 2 values:

First, a string of this format: "first_name last_name the warrior"
Second, the power input after adding 1 to it.


For example:

"""