# ------------------------------------------ #
#
# -- If Else practice -- Python StudySpace --
#
# ------------------------------------------ #

"""
Here are some basic rules with if/else blocks.

You can't have an elif or an else without an if
You can have an else without an elif

Remember, to check if two values are the same use the == operator.

"""

same = 5 == 6
# same is false

same = 6 == 6
# same is true

# ------------------------------- #
# -- Assignment -- Practice --
# ------------------------------- #

"""
There is a bug in the check_high_score function! Add the proper conditional 
statement to fix the bug. 

If the names match, "You are the highest scoring player!" 
should be returned. Otherwise, "You are not the highest scoring player!" should be 
returned.

"""

# ------------------------------ #
# -- Buggy Code --
# ------------------------------ #

def check_high_score(current_player_name, high_scoring_player_name):
    if True:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"