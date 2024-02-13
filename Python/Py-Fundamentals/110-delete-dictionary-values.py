# --------------------------------------------- #
#
# -- Deleting Dictionary Values --
#
# --------------------------------------------- #

# You can delete existing keys using the del keyword.

names_dict = {
    'jack': 'bronson',
    'jill': 'mcarty',
    'joe': 'denver'
}

del names_dict['joe']

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}



"""
Notice that if you try to delete a key that doesn't exist, you'll get an error.

"""