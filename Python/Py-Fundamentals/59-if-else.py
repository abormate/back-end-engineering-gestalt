# -------------------------------------- #
#
# -- If Else -- Python StudySpace
#
# -------------------------------------- #

"""
An if statement can be followed by zero or more elif (which stands for "else if") 
statements, which can be followed by zero or one else statement.

For example:

if score > high_score:
    print('High score beat!')
elif score > second_highest_score:
    print('You got second place!')
elif score > third_highest_score:
    print('You got third place!')
else:
    print('Better luck next time')


-------------------------------------------

First the if statement is evaluated. If it is True then the if statement's body is 
executed and all the other elses are ignored.

If the first if is false then the next elif is evaluated. Likewise, if it is True 
then its body is executed and the rest are ignored.

If none of the if statements evaluate to True then the final else statement will be 
the only body executed.

"""

# -------------------------- #
# -- Assignment -- Practice --
# -------------------------- #

"""
Complete the player_status function. If the player's health less than or equal to 0, 
return the string:

dead

Otherwise, if it's less than or equal to 5 return the string:

injured

Otherwise, return the string:

healthy


"""

# -------------------------- #
# -- Buggy Code --
# -------------------------- #

def player_status(health):
    pass

