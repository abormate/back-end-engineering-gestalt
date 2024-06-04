# ------------------------------------------ #
#
# -- Concatenate -- Python LearnSpace --
#
# ------------------------------------------ #

"""
The + operator doesn’t just add two numbers, it can also “add” two 
strings! The process of combining two strings is called string 
concatenation. Performing string concatenation creates a brand 
new string comprised of the first string’s contents followed by 
the second string’s contents (without any added space in-between).

"""

greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"
print(full_text)

"""
In this sample of code, we create two variables that hold strings 
and then concatenate them. But we notice that the result was 
missing a space between the two, lets add the space in-between 
using the same concatenation operator!

"""

full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)

