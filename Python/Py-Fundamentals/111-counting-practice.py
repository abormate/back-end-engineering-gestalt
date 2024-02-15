# --------------------------------------------- #
#
# -- Counting Practice -- Python StudySpace --
#
# --------------------------------------------- #

# If you're unsure whether or not a key exists in a dictionary, use the in keyword.

cars = {
    'ford': 'f150',
    'tesla': '3'
}

print('ford' in cars)
# Prints: True

print('gmc' in cars)
# Prints: False

# ---------------------------------- #
# -- Assignment -- Practice --
# ---------------------------------- #

"""
We need to be able to report to our players how many friends are in their 
immediate vicinity - but they want the count of each enemy by its kind. 

Complete the count_friends function. It takes a list of friends names as input. 

It should return a dictionary where the keys are all the friends names from the list, 
and the values are the counts of how many times each friend appeared in the list.

"""

# ----------------------------------- #
# -- Buggy Code --
# ----------------------------------- #

def count_friends(friend_names):
    pass

# ----------------------------------- #
# -- Worked on Code -- Count Enemies
# ----------------------------------- #

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict