item_list = []
item_dict = {}

while True:
    try:
        inp = input().upper()
        item_list.append(inp)
    except EOFError:
        print("")
        for item in item_list:
            if item not in item_dict:
                item_dict[item] = 1
            else:
                item_dict[item] += 1
        for key, value in sorted(item_dict.items()):
            print(f"{value} {key}")
        exit()
