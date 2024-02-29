# ---------------------------------------- #
#
# -- Sets Quiz -- Python StudySpace --
#
# ---------------------------------------- #

"""
Sets are like Lists, but they are unordered and they guarantee uniqueness. Only 
ONE of each value can be in a set.

"""

fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

# --------------------------------------- #
# -- Value Add --
# --------------------------------------- #

fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

# --------------------------------------- #
# -- Empty Set --
# --------------------------------------- #

"""
Because the {} syntax creates an empty dictionary, to create an empty set, just 
use the set() function.

"""

fruits = set()
fruits.add('pear')
print(fruits)
# Prints: {'pear'}

# -------------------------------------- # 
# -- Iterate over values in a Set --
# -------------------------------------- #

# !! NOTE !! -- Order is not guaranteed

fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple

# ------------------------------------- #
#
# ------------------------------------- #