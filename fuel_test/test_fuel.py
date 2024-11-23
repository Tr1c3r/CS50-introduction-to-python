# Importing necessary functions and modules
from fuel import convert
from fuel import gauge
import pytest

# Main function to run tests
def main():
    test_convert()
    test_gauge()

# Test function for the 'convert' function
def test_convert():
    # Testing for ValueError with invalid fraction
    with pytest.raises(ValueError):
        convert("3/2")

    # Testing for ValueError with non-numeric characters
    with pytest.raises(ValueError):
        convert("a/b")

    # Testing for ZeroDivisionError with denominator being zero
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

    # Testing conversion for valid fractions
    assert convert("3/3") == 100
    assert convert("0/3") == 0
    assert convert("1/2") == 50

# Test function for the 'gauge' function
def test_gauge():
    # Testing gauge function with different percentages
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
