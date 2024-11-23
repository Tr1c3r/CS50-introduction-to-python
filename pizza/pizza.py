import tabulate
import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")

    elif len(sys.argv) < 2:
        sys.exit("Too few arguments")

    csv = sys.argv[1]

    if not csv.endswith(".csv") and it_exists(csv) == False:
        sys.exit("Not a CSV file")

    prices = []
    with open(csv, 'r') as file:
        for line in file:
            pizza, small, large = line.rstrip().split(",")
            prices.append([pizza, small, large])
    table = tabulate.tabulate(prices, headers="firstrow", tablefmt="grid")
    print(table)

def it_exists(check_file):
    # Check if the file exists
    try:
        with open(check_file, 'r'):
            pass
        return True
    except FileNotFoundError:
        return False

if __name__ == '__main__':
    main()
