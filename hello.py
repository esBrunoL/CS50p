# This script will ask for the user's name and greet them.

# Variables in python dont need to be declared before use.
name = input("What's your name? ")

# Use str methods to remove white space from str and capitalize user's input.
name = name.strip().title()

#Split user's name into first and last name.
# The split() method splits a string into a list where each word is a list item.
first, last =  name.split(" ")     

# Output a greeting message
# f-string allows embedding expressions inside string literals, using curly braces {}.
print(f"Hello, {name}", end="!\n")