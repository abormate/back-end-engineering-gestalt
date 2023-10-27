# -------------------------------------- #
#
# -- Where to Declare Functions -- Python StudySpace --
#
# -------------------------------------- #

"""
You've probably noticed that a variable needs to be declared before it's used. For example, the following doesn't work

print(my_name)
my_name = 'Lane'

"""

# It needs to be this

my_name = 'Lane'
print(my_name)


"""
Lines of code execute in order from top to bottom, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that 
function until after the definition.

The main() function is a convention used in many programming languages to specify the entrypoint of an application. By defining a single main function, and only calling main() 
at the end of the entire program we ensure that all of our functions are defined before they're called.

"""

# -------------------------- #
# -- Assignment -- Practice 
# -------------------------- #

# There is a bug in our program! Fix it.

# -------------------------- #
# -- Buggy Code --
# -------------------------- #

# main()


def main():
    print("Side Quest is booting up...")


# -------------------------- #
# -- Fixed Code --
# -------------------------- #

def main():
    print("Side Quest is booting up...")

main()