from um import count

def test_count():
    assert count('Hello, um, world') == 1
    assert count('num dum dumb') == 0
    assert count('um um um') == 3
    assert count('This is dumb not um') == 1
    assert count('um uM Um UM') == 4

if __name__ == "__main__":
    test_count()
