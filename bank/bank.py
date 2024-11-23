# First, the user's greetigs
gr = str.lower(input("Greeting:")).strip()

# Starting to decompose the message
mny100 = gr.startswith("hello")

mny20 = gr.startswith("h")

# Conditional 1
if mny100 == True:
    print("$0")

# Conditional 2
elif mny20 == True and mny100 == False:
    print("$20")

else:
    print("$100")