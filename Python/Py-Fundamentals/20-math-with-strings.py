# -------------------------------------- #
#
# -- Math with Strings -- Python StudySpace
#
# -------------------------------------- #

"""
Most of the math operators we went over earlier don't work with strings, aside from the + addition operator. When working with strings the + operator 
performs a "concatenation".

"Concatenation" is a fancy word that means the joining of two strings.

"""

first_name = "Lane "
last_name = "Lane"
full_name = first_name + last_name

""""
full_name now holds the value "Lane Lane".

Notice the extra space at the end of "Lane " in the first_name variable. That extra space is there to separate the words in the final result: "Lane Wagner".

"""

# --------------------------- #
# -- Assignment -- Practice --
# --------------------------- #

"""
We have a second player in our game!

We need to tell each of our players how much health they have left.

Edit line 9 to print Player 1's health: You have 1200 health using string concatenation and the variables provided
Edit line 10 to print Player 2's health: You have 1100 health in the same way

"""

# --------------------------- #
# -- Old buggy code --
# --------------------------- #


sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print()
print()


# --------------------------- #
# -- New fixed code --
# --------------------------- #

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)