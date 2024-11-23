# This is the price of the can of coke
Price = 50

# We start the loop so the code repeats itself until the coke is payed
while Price > 0:
        print(f"Amount Due: {Price}")
        # Cent equals the coin that the user is inserting
        cent = int(input("Insert Coin:"))
        # In here we make sure that the coin inserted is one of the coins that the machine accepts
        if cent == 10 or cent == 25 or cent == 5:
                # Then, we subtract the amount that was put to see how much is left to pay
                Price -= cent

# The change owed is the result of the last subtraction in the absolute value so we can see clearly the amount in a positive number
print(f"Change Owed: {abs(Price)}")