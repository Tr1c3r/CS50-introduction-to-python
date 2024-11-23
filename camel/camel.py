# Prompts the user for a camelcase variable name
camelcase = input("camelCase: ")
# With this line of code we get rid of the cap letters and it ads a "_" every time there was one
# Strip takes out the "_" that may have appeared at the start of the variable's name
camelcase = "".join(["_" + a.lower() if a.isupper() else a for a in camelcase]).strip("_")
print(f"snake_case: {camelcase}")