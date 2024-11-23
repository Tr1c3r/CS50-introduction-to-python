def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # We put the parameters of the plates in a conditional
    # Len is to count how many character the string has
    # .isalpha returns 'true' if the first 3 characters are alphabetic ones
    # .isalnum returns 'true' if all the characters in the string are alphanumeric ones
    # With those parameters we make sure that it has: 6 characters max and 2 min, the 3 first are letters and it has no
    # characters like '@' or '$'
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum:
        for ch in s:
            # We check if the character is a digit
            if ch.isdigit():
                # If it is a digit, we save in the variable 'r' the position of it
                r = s.index(ch)
                # With this conditional we check if the remaining characters after the found digit are also digits different to 0
                # This way we make sure that after a number, there are no letters
                if s[r:].isdigit() and int(ch) != 0:
                    return True
                else:
                    return False
        return True

main()