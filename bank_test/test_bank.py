from bank import value

def test_bank():
    assert value("WHatS Up") == 100
    assert value("JEllo") == 100
    assert value("Hey") == 20
    assert value("Hello") == 0