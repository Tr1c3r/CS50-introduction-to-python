from numb3rs import validate

def test_numb3rs():
    assert validate('127.127.23.0') == True
    assert validate('127.127.23.2') == True
    assert validate('300.127.23.0') == False
    assert validate('255.300.23.0') == False
    assert validate('255.127.500.0') == False
    assert validate('255.127.23.400') == False
    assert validate('f.127.23.0') == False
    assert validate('255.127.23.40.40') == False
    assert validate('....') == False
