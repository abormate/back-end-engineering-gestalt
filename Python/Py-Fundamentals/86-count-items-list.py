# ------------------------------------------- #
#
# -- Counting the items in a List -- 
#
# ------------------------------------------- #

"""
Remember that we can iterate (count) over all the elements in a list using a loop. 
For example, the following code will print each item in the sports list.

"""

# for i in range(0, len(sports)):
#    print(sports[i])


# ---------------------------- #
# -- Assignment -- Practice --
# ---------------------------- #

"""
Our players need a way to see how many copies of a specific item they have within 
their inventory!

Let's finish the get_item_counts function. Within the loop, count how many times 
Potion, Bread, and Shortsword appear by incrementing the potion_count, 
bread_count and shortsword_count variables respectively.

"""

# --------------------------- #
# -- Buggy Code --
# --------------------------- #

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        pass

    # don't touch below this line

    return potion_count, bread_count, shortsword_count

