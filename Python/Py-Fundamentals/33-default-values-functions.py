# --------------------------------------- #
#
# -- Default Values for Function Arguments --
#
# --------------------------------------- #

"""
Python has a way to specify a default value for function arguments. This can be convenient if a function has arguments that are essentially "optional", and you as the 
function creator want to use a specific default value in case the caller doesn't provide one

A default value is created by using the assignment (=) operator in the function signature.

"""

def get_greeting(email, name="there"):
    return f"Hello {name}, welcome! You've registered your email: {email}"

# case 01
msg = get_greeting("lane@example.com", "Lane")
# Hello Lane, welcome! You've registered your email: lane@example.com

# case 02
msg = get_greeting("lane@example.com")
# Hello there, welcome! You've registered your email: lane@example.com

"""
If the second parameter is omitted, the default "there" value will be used in its place. As you may have guessed, for this structure to work, optional arguments that 
have defaults specified come after all the required arguments.

"""

# ----------------------------- #
# -- Assignment -- Practice --
# ----------------------------- #

"""
Complete both the get_punched and get_slashed functions. They should each take 2 arguments:

health: An integer
armor: An integer

They should each return a single integer: the new health value after the attack has been applied. Getting punched should result in 50 - armor health being lost. 
Getting slashed should result in 100 - armor health being lost. In other words, getting slashed should do around twice as much damage as getting punched.


However, if no armor is passed into the function the armor should default to 0.

"""