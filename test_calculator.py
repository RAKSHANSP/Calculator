from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(5, 0) == "Error"

from calculator import calculate_all

def test_calculate_all():
    result = calculate_all(10, 2)
    assert result["add"] == 12
    assert result["subtract"] == 8
    assert result["multiply"] == 20
    assert result["divide"] == 5

def test_power():
    assert power(2, 3) == 8

