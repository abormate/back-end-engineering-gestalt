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
