# ------------------------------------ #
#
# -- Filter Messages -- Python StudySpace --
#
# ------------------------------------ #

"""
You are about to write a bit more code in a single function than you have before.

Do not try to write it all at once. Start with the outermost loop, and work your 
way inwards. Add extra print() statements and run your code often to make sure 
it's doing what you expect. Just make sure to remove the extra print() 
statements before submitting your code.

Running your code often to make sure each line is doing what you expect is called 
"debugging". All programmers, even seasoned professionals, break large problems 
down into small ones that they can debug line by line.


"""

# --------------------- #
# -- Assignment --
# --------------------- #

"""
We need to filter the profanity out of our game's live chat feature! Complete the 
filter_messages function. It takes a list of chat messages as input and returns 2 
new lists:

"""

messages = ["dang it bobby!", "look at it go"]
# filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

"""
Here are the steps for you to follow:

1. Create the 2 empty lists that you'll return at the end. One for the filtered messages, and one for counts of words removed.
2. For each message in the input list:

-- -- Split the message into a list of words using the .split() string method (see below for help).
-- -- Create a new empty list for all the non-bad words for this message.
-- -- Create a counter variable and set it to 0. We'll increment this when we remove words from this message.
-- -- For each word in the message:

-- -- -- If the word is dang, increment the counter
-- -- -- If it is not dang, add the word to the non-bad word list you created

-- -- Join the list of non-bad words into a single string using the .join() method (see below for help)
-- -- Append the new clean message to the final list of filtered messages
-- -- Append the count of bad words removed to its list
-- -- Return the filtered messages first, then the counters

"""

# --------------------------- #
# -- Tips for Solving Problem --
# --------------------------- #

"""
The .split() method is called on a string. If you don't pass it any arguments, it 
will just split the words in the string on the whitespace.

"""

message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]

"""
The .join() method is called on a delimiter (what goes between all the words in 
the list), and takes a list of strings as input.

"""

list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"

# ------------------------------ #
# -- Buggy Code --
# ------------------------------ #

def filter_messages(messages):
    pass

# ------------------------------ #
# -- Unit Tester --
# ------------------------------ #

from main import *

run_cases = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
]

submit_cases = run_cases + [
    (
        [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 2, 1, 0, 0, 0, 1],
    ),
]


def test(input, expected_output1, expected_output2):
    print("---------------------------------")
    print(f"Input:")
    print(f" * messages: {input}")
    print("Expecting:")
    print(f" * filtered messages: {expected_output1}")
    print(f" * words removed: {expected_output2}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" * filtered messages: {result[0]}")
        print(f" * words removed: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    if result == (expected_output1, expected_output2):
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

# ------------------------------------- #
# -- Worked on Code --
# ------------------------------------- #

def filter_messages(messages):
    filtered_messages = []
    words_removed = []
    for message in messages:
        words = message.split()
        new_words = []
        removed = 0
        for word in words:
            if word == "dang":
                removed += 1
            else:
                new_words.append(word)
        filtered_messages.append(" ".join(new_words))
        words_removed.append(removed)

    return filtered_messages, words_removed