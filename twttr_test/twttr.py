def shorten(word):
    # We list in an array all the characters that we want to remove
    r = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # We create the variable 'Output' with no content
    out = ""

    # We create the loop
    for char in word:
        # Conditional to see in each character if there's one of the list to remove it
        if char not in r:
            out += char
    return out


if __name__ == "__main__":
    # Prompts the input
    user_input = input("Input: ")
    # We print the result
    print(f"Output: {shorten(user_input)}")
