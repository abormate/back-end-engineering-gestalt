# -------------------------------------------- #
#
# -- Range Continued -- Python StudySpace --
#
# -------------------------------------------- #

"""
The range() function we've been using in our for loops actually has an optional 
3rd parameter: the "step".

"""

for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8
    
"""
The "step" parameter determines how much to add to i in each iteration of the 
loop. You can even go backwards:

"""

for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1
