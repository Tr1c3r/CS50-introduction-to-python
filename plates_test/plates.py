def main():
    # Prompt user for a license plate input
    plate = input("Plate: ")

    # Check if the entered plate is valid using the is_valid function
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of the plate is between 2 and 6 characters
    # Check if the first two characters are alphabetical
    # Check if all characters are alphanumeric
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        # Iterate through each character in the plate
        for ch in s:
            # Check if the character is a digit
            if ch.isdigit():
                # Get the index of the digit in the plate
                r = s.index(ch)

                # Check if the remaining part of the plate is composed of digits
                # Check if the digit is not 0
                if s[r:].isdigit() and int(ch) != 0:
                    return True  # Plate is valid
                else:
                    return False  # Plate is invalid
        return True  # All checks passed, plate is valid
    else:
        return False  # Plate length or format is invalid


if __name__ == "__main__":
    main()
