def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    get_order(menu)

def get_order(menu):
    money = 0
    while True:
        try:
            ask = input("Order: ").title()
            if ask in menu:
                money += menu[ask]
                print(f"Total: ${money:.2f}")
            else:
                pass
        except (EOFError):
            return money

if __name__ == "__main__":
    main()