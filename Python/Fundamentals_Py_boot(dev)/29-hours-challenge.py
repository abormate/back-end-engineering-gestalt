# -------------------------------------- #
#
# -- Hours to Seconds -- Python StudySpace --
#
# -------------------------------------- #

"""
We need to be able to display the current in-game time in seconds to our players!

Write the convert_hours_to_seconds function. It should convert hours to seconds.

"""

# ------------------------- #
# -- Set up Code --
# ------------------------- #

# def convert_hours_to_seconds(hours):
    # ?


# Don't touch below this line


def test(hours):
    secs = convert_hours_to_seconds(hours)
    print(f"{hours} hours is {secs} seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)


# ----------------------- #
# -- Debugged Code --
# ----------------------- #

def convert_hours_to_seconds(hours):
    return hours * 3600


# Don't touch below this line


def test(hours):
    secs = convert_hours_to_seconds(hours)
    print(f"{hours} hours is {secs} seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)