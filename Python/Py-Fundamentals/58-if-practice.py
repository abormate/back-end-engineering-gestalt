# -------------------------------------- #
#
# -- If Practice -- Python StudySpace --
#
# -------------------------------------- #

# Remember, you can use the == operator to check if two values are equal. 
# For example:

is_equal = 5 == 5
# is_equal is True

# ----------------------------- #
# -- Assignment -- Practice
# ----------------------------- #

"""
Complete the check_swords_for_army function. If the number of swords and the 
number of soldiers match, return the string:

"""

# correct amount

# Otherwise, return the string:

# incorrect amount


# ----------------------------- #
# -- Repaired Code --
# ----------------------------- #

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    return "incorrect amount"