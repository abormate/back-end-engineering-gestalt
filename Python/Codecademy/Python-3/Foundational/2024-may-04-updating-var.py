# --------------------------------------------- #
#
# -- Python LearnSpace -- Updating Variables --
#
# --------------------------------------------- #

"""
Variables that are assigned numeric values can be treated the same as the 
numbers themselves. Two variables can be added together, divided by 2, and 
multiplied by a third variable without Python distinguishing between the 
variables and literals (like the number 2 in this example). Performing 
arithmetic on variables does not change the variable — you can only update 
a variable using the = sign.


"""

coffee_price = 1.50
number_of_coffees = 4

# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price 
coffee_price = 2.00

# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
