# We make a dict with all fruits and their calories
fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
    }
# Then we prompt the user to input a fruit. It has to be exactly like in the list
input = str.lower(input("What is your fruit? ")) # This will take whatever the user types and turns it into lowercase

# We insert a conditional to see if the input is equal to an element of the list
if input in fruits:
    print("Calories:", fruits[input])