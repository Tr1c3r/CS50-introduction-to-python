import pytest
from working import convert

def test_convert():
    assert convert('09 AM to 05 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 PM to 5 AM') == '21:00 to 05:00'
    assert convert('9 AM to 10 AM') == '09:00 to 10:00'

    with pytest.raises(ValueError):
        convert('9 AM 10 AM')

    with pytest.raises(ValueError):
        convert('13 PM to 10 AM')

    with pytest.raises(ValueError):
        convert('14:90 PM to 10 AM')

if __name__ == "__main__":
    test_convert()
