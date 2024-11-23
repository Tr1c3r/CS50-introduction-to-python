
# We start with the input of the hour
def main():
    time = input("What hour is it? ")

# We use "convert" so we can turn our str into a float value
    meal = convert(time)

# Conditionals for each food
    if meal >=7 and meal <= 8:
        print ("breakfast time")

    elif meal >= 12 and meal <= 13:
        print("lunch time")

    elif meal >= 18 and meal <= 19:
        print("dinner time")

    else:
        print("")

# We make the function convert
def convert(t):
    hour, min = t.split(":")
    hour = float(hour)+float(min)/60
    return hour

if __name__ == "__main__":
    main()