import datetime
from seasons import Birthday, Spell

def test_valid_birthday():
    user_birthday = Birthday(2000, 0o5, 20)
    assert user_birthday.minutes_lived() != None

def test_invalid_birthday():
    try:
        Birthday(200, 20, 20)
    except ValueError:
        pass

def test_spell():
    num = 100
    testing_spell = Spell().spell(num)
    assert testing_spell == 'One hundred'

if __name__ == "__main__":
    import pytest
    pytest.main()
