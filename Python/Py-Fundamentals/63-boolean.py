# ------------------------------------- #
#
# -- If and Boolean Practice -- 
#
# ------------------------------------- #

"""
In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer 
refills their stamina!

Complete the function that determines if a bartender should serve drinks to a 
customer. The function should return True only if all the following conditions 
are met:

The time is between 5 and 10 both inclusive
The bartender is not on break
The customer's age is 21 or older.


If any of these conditions are not met the function should return False.

"""

# ------------------------ #
# -- Practice --
# ------------------------ #

def should_serve_customer(customer_age, on_break, time):
    pass

def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21 and on_break == False and time <= 10 and time >= 5:
        return True
    else:
        return False