# Prompt the message to interpretate
expression = input("Expression: ")

# Split into variables
x, y ,z = expression.split(" ")

# For dividing
if y == "/":
    res = float(x)/float(z)
    print (res)

# For multiplying
elif y == "*":
    res = float(x)*float(z)
    print (res)

# For subtracting
elif y == "-":
    res = float(x)-float(z)
    print (res)

# For sum
elif y == "+":
    res = float(x)+float(z)
    print (res)