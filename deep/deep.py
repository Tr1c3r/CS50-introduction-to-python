# Asks the big question
Q = (input("What's the meaning of life? "))

# Correction to a more basic word
Q2 = Q.lower().replace("-","").replace(" ","")

#Conditional
if Q2 == "42" or Q2 == "fortytwo":
    print("Yes")
else:
    print("No")