from jar import Jar

def test_valid_capacity():
    jar = Jar(capacity=10)
    assert jar.capacity == 10

def test_invalid_capacity():
    try:
        Jar(capacity=-10)
    except ValueError:
        pass

def test_deposit():
    jar = Jar(capacity=10)
    jar.deposit(5)
    assert jar.size == 5

    try:
        jar.deposit(-5)
    except ValueError:
        pass

def test_withdraw():
    jar = Jar(capacity=10)
    jar.deposit(9)
    jar.withdraw(5)
    assert jar.size == 4

    try:
        jar.deposit(4)
        jar.withdraw(-20)
    except ValueError:
        pass

if __name__ == "__main__":
    import pytest
    pytest.main()
