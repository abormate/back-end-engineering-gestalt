# --------------------------------------- #
#
# -- Variable Types -- Python StudySpace --
#
# --------------------------------------- #

# Python has several basic data types

# -------------------------- #
# -- String Type --
# -------------------------- #

"""
"Strings" are raw text in coding speak. They are called "strings" because they are a list of characters strung together. Strings are declared in Python by 
using single quotes or double quotes. That said, for consistency's sake, we prefer double quotes.

"""

name_with_single_quotes = 'boot.dev'
name_with_double_quotes = "boot.dev"

# -------------------------- #
# -- Numeric Types --
# -------------------------- #

# Numbers aren't surrounded by quotes when created, but they can have decimals and negative signs.


# -------------------------- #
# -- Integers are numbers without decimals --
# -------------------------- #

x = 5
y = -5

# -------------------------- #
# -- A "float" is a number with a decimal --
# -------------------------- #

x = 5.2
y = -5.2

# -------------------------- #
# -- Boolean Type --
# -------------------------- #

0 = False
1 = True

is_tall = True

# -------------------------- #
# -- Assignment -- Practice --
# -------------------------- #

"""
Fix the bugs in the code to move on. player_health should be an integer and player_has_magic should be a boolean.

"""

player_health = "100"

player_has_magic = "True"

# don't touch below this line
print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")