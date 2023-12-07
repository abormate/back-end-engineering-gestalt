# ---------------------------------------- #
#
# -- If Else Practice -- 
#
# ---------------------------------------- #

"""
Here are some basic rules with if/else blocks.

-- You can't have an elif or an else without an if
-- You can have an else without an elif

"""

# --------------------------- #
# Assignment -- Practice
# --------------------------- #

"""
Complete the check_high_score function. If the player_name matches the high score 
name, return the string:

-- High


Otherwise, if it's the low scorer, return the string:

-- Low

Otherwise, return the string:

-- Neither

"""

# --------------------------- #
# -- Buggy Code --
# --------------------------- #

# --------------------------- #
# -- Repaired Code --
# --------------------------- #

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"