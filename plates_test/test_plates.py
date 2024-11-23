from plates import is_valid


def main():
    plates_test()


def test_plates():
    assert is_valid("TO5410") == True # Valid
    assert is_valid("AAA22A") == False # Invalid: it has a letter after a number
    assert is_valid("AAAAAAA") == False # Invalid: goes over the limit of characters (6)
    assert is_valid("AAA02") == False # Invalid: first number can't be a 0
    assert is_valid("@@@") == False # Invalid: only alphanumeric characters
    assert is_valid("123XYZ") == False # Invalid: it has letters after a number
    assert is_valid("123") == False # Invalid: doesn't have letters
    assert is_valid("A@12") == False # Invalid: only alphanumeric characters
    assert is_valid("1XYZ") == False # Invalid: it has letters after a number
    assert is_valid("CS.5") == False # Invalid: only alphanumeric characters


if __name__ == "__main__":
    main()
