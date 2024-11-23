import sys
import csv

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")

    # Initialize lists to store data from the CSV file
    first_names = []
    last_names = []
    houses = []

    try:
        # Open the input CSV file in read mode
        with open(sys.argv[1], 'r') as csvfile:
            # Create a CSV reader object
            reader = csv.DictReader(csvfile)

            # Iterate through each row in the input CSV file
            for row in reader:
                # Extract first and last names from the 'name' column
                last, first = row['name'].split(", ")
                house = row['house']  # Get the 'house' value from the row
                # Append the extracted values to their respective lists
                first_names.append(first)
                last_names.append(last)
                houses.append(house)

        # Open the output CSV file in write mode
        with open(sys.argv[2], 'w', newline='') as newcsv:
            # Specify the field names for the output CSV file
            fieldnames = ['first', 'last', 'house']
            # Create a CSV writer object
            writer = csv.DictWriter(newcsv, fieldnames=fieldnames)
            # Write the header row to the output CSV file
            writer.writeheader()

            # Iterate through the lists and write rows to the output CSV file
            for i in range(len(first_names)):
                writer.writerow({'first': first_names[i], 'last': last_names[i], 'house': houses[i]})

    except FileNotFoundError:
        sys.exit("CSV file not found")

if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
