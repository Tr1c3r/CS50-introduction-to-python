def main():
    # We define x with the function 'get int'
    x = get_int()
    print(f"{x}")

    # We loop the prompt to get an usable answer
def get_int():
    while True:
        try:
            # Prompt the user to get the fraction and split it by the slash
            fraction = input("Fraction: ").split("/")

            # Simple calculus to get a value as a porcentage
            re = float(int(fraction[0]) / int(fraction[1]) * 100)
            # Num number can't be bigger than den number, so we make this conditional
            if int(fraction[0]) <= int(fraction[1]):

                # We start putting the conditionals of the problem
                if re <= 1:
                    print("E")

                elif re >= 99:
                    print("F")

                else:
                    print(f"{round(float(re))}%")
                exit()
            else:
                return get_int()

        except (ValueError, ZeroDivisionError):
            pass

main()