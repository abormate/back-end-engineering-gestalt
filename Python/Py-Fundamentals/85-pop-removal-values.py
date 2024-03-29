# ---------------------------------------- #
#
# -- Pop Removal of Values -- Python StudySpace --
#
# ---------------------------------------- #

"""
.pop() is the opposite of .append(). Pop removes the last element from a list and 
returns it for use. For example:

"""

vegetables = ["broccoli", "cabbage", "kale", "tomato"];
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'


# ---------------------------- #
# -- Assignment -- Practice --
# ---------------------------- #

"""
Our player is selling the items in their inventory to the shopkeep!

Pop the last element from the inventory list until there is nothing left. Pop the 
elements into an item variable so that each prints in turn on line 19.

"""

# ---------------------------- #
# -- Buggy Code --
# ---------------------------- #

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        # ?

        # don't touch below this line
        # print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()

# ----------------------------- #
# -- Functional Repaired Code --
# ----------------------------- #

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        # ?

        # don't touch below this line
       # print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()
