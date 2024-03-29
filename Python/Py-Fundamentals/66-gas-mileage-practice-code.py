# ------------------------------------------- #
#
# -- Gas Mileage -- Practice Coding --
#
# ------------------------------------------- #

"""
There isn't a gas station between Tyler's house and his work. He is trying to 
figure out if his car has enough gas to get him to work and back home.

"""

# ----------------------- #
# -- Practice --
# ----------------------- #

"""
Complete the has_enough_gas function.

Do some Pythonic math to determine how many gallons are needed for Tyler to get to 
work AND make it back home after he gets off work. Assign the result to a 
gallons_needed variable.

Return True if there are at least enough gallons in the tank based on the 
gallons_needed variable, and False otherwise.

"""

def has_enough_gas(gallons_in_car, miles_to_work, miles_per_gallon):
    gallons_needed = (2 * miles_to_work) / miles_per_gallon
    if gallons_in_car >= gallons_needed:
        return True
    else:
        return False
