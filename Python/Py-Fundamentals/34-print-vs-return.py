# ----------------------------------------- #
#
# -- Printing vs Returning -- Python StudySpace
#
# ----------------------------------------- #

"""
Some new developers get hung up on the difference between print() and return.

It can be particularly tricky when the test suite we provide prints the output of your 
functions to the console. This makes it seem like print() and return are interchangeable, 
but they are not!

print(): A function that prints a value to the console. It does not return a value.
return: A keyword that returns a value from a function (back to the caller of the function). 

It does not print anything to the console.



PRINTING TO DEBUG YOUR CODE


Printing values and running your code in the console is a great way to debug your code. 
You can see what values are stored in various variables, find your mistakes, and fix them. Add print statements and run your code as you go! It's a great habit to get into to make sure that each line you write is doing what you expect it to do.

In the real world it's rare to leave print() statements in your code once you're done 
debugging. Similarly, you need to remember to remove any print() statements from your 
code before submitting your work for review here on Boot.dev because it will interfere 
with the test suite!

"""

# ------------------------- #
# -- Assignment -- Practice --
# ------------------------- #

"""
There is a problem in the get_title function! It's supposed to calculate the title value 
and return it to the caller. Instead it's barbarically printing the value to the console.


Fix the function so that it returns the title value instead of printing it.

"""

# ------------------------- #
# -- Buggy Code --
# ------------------------- #

def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    print(title)


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Job: {job}")
    print(f"Title: {title}")
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragon", "Son of Arathorn", "ranger")