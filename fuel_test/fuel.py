def main():
    inp = input("Fraction: ")
    conv = convert(inp)
    print(gauge(conv))


def convert(fraction):
    split = fraction.split("/")
    x = int(split[0])
    y = int(split[1])

    if y == 0:
        raise ZeroDivisionError
    elif is_not_integer(x) or is_not_integer(y) or x > y:
        raise ValueError
    else:
        conversion = int(round(float((x/y)*100)))
        return conversion

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        Z = f"{percentage}%"
        return Z

def is_not_integer(variable):
    return not isinstance(variable, int)

if __name__ == "__main__":
    main()
