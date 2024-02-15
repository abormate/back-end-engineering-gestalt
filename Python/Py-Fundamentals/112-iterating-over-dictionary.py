# ----------------------------------------------- #
#
# -- Iterating over a Dictionary -- Python StudySpace --
#
# ----------------------------------------------- #

fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny