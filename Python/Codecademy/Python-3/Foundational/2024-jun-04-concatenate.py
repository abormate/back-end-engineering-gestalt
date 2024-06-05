# ------------------------------------------ #
#
# -- Concatenate -- Python LearnSpace --
#
# ------------------------------------------ #

"""
The + operator doesnt just add two numbers, it can also “add” two 
strings! The process of combining two strings is called string 
concatenation. Performing string concatenation creates a brand 
new string comprised of the first strings contents followed by 
the second strings contents (without any added space in-between).

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


"""
Now the code prints the message we expected.

If you want to concatenate a string with a number you will need 
to make the number a string first, using the str() function. If 
youre trying to print() a numeric variable you can use commas to 
pass it as a different argument rather than converting it to a 
string.

"""

birthday_string = "I am "
age = 9
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)


