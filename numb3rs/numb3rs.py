import re

def main():
    # Prompt the user to enter an IPv4 address and print the result of validation
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        # Define a list of valid numbers for each segment of an IPv4 address (0 to 255)
        valid_n = list(range(0, 256))

        # Use regular expression to match and capture each segment of the IPv4 address
        matches = re.fullmatch(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', ip)

        if matches:
            # Extract the matched segments and convert them to integers
            groups = [int(matches.group(i)) for i in range(1, 5)]

            # Check if all segments are within the valid range
            if all(num in valid_n for num in groups):
                return True  # If all conditions are met, the IP address is valid
            else:
                return False  # If any segment is out of range, the IP address is invalid
        else:
            raise AttributeError  # If the regex does not match, raise an AttributeError

    except AttributeError:
        return False  # Handle the AttributeError by returning False (invalid IP address)

if __name__ == "__main__":
    main()

# _______               __     __
#|_     _|.-----.-----.|  |--.|__|
#  |   |  |  _  |__ --||     ||  |
#  |___|  |_____|_____||__|__||__|
