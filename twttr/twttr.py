# Prompts the input
Input = input("Input: ")

# We list in an array all the characters that we want to remove
r = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# We create the variable 'Output' with no content
Output = ""

# We create the loop
for i in Input:
    # Conditional to see in each character if there's one of the list to remove it
    if not i in r[:]:
        Output += i

# We print the result
print(f"Output: {Output}")