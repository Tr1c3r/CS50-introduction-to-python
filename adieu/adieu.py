import inflect

# Create an inflect engine for text manipulation
p = inflect.engine()

try:
    names = []  # Initialize an empty list to store names
    while True:
        # Prompt the user for a name and capitalize it
        name = str.title(input("Name: "))

        # Check if the input name is empty (user pressed Enter with no input)
        if not name:
            break  # If empty, exit the loop

        # Append the capitalized name to the 'names' list
        names.append(name)
except EOFError:
    pass  # Handle the case where the user presses Ctrl+D (EOF)

# Use the inflect engine to join the list of names into a single string
name_list = p.join(names)

# Print the farewell message with the joined name list
print(f"\nAdieu, adieu, to {name_list}")
