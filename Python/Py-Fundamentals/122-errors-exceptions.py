# -------------------------------------------------- #
#
# -- Python StudySpace -- Errors and Exceptions --
#
# -------------------------------------------------- #

"""
You've probably encountered some errors in your code from time to time if you've 
gotten this far in the course. In Python, there are two main kinds of 
distinguishable errors.

-- syntax errors
-- exceptions

"""

# ------------------------ #
# -- Syntax Errors --
# ------------------------ #

"""
You probably know what these are by now. A syntax error is just the Python 
interpreter telling you that your code isn't adhering to proper Python syntax.

"""

# this is not valid code, so it will error

# ----------------------- #
# -- Exceptions --
# ----------------------- #

"""
Even if your code has the right syntax, however, it may still cause an error 
when an attempt is made to execute it. Errors detected during execution are 
called "exceptions" and can be handled gracefully by your code. You can even 
raise your own exceptions when bad things happen in your code.

Python uses a try-except pattern for handling errors.

"""

try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"
  
  