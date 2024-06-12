# --------------------------------------------- #
#
# -- Python LearnSpace -- Multiple Line Strings --
#
# --------------------------------------------- #

"""
Python strings are very flexible, but if we try to create a string 
that occupies multiple lines we find ourselves face-to-face with a 
SyntaxError. 

Python offers a solution: multi-line strings. By using 
three quote-marks instead of one, we tell the program that the 
string doesnt end until the next triple-quote. This method is 
useful if the string being defined contains a lot of quotation 
marks and we want to be sure we dont close it prematurely.

"""

<<<<<<< HEAD
"""
In the above example, we assign a famous poets words to a variable. 
Even though the quote contains multiple linebreaks, the code works!
=======
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
>>>>>>> 4d4a3fca35214c1a19f5ade6153cf8ad50ba191e

If a multi-line string isnt assigned a variable or used in an 
expression it is treated as a comment.


"""

# Assign the string here

to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""


print(to_you)
