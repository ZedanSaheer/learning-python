import pytest
from calculator import square


def main():
    test_negative_square()
    test_positive_square()
    test_zero_square()


def test_positive_square():
    assert square(2) == 4
    assert square(3) == 9

def test_negative_square():
    assert square(-3) == 9
    assert square(-2) == 4

def test_zero_square():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()
