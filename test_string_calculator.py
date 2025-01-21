import pytest
from string_calculator import StringCalculator  # Replace with your filename

def test_empty_string_returns_zero():
    calculator = StringCalculator()
    assert calculator.add("") == 0, "Empty string should return 0"

def test_single_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1, "'1' should return 1"

def test_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,5") == 6, "'1,5' should return 6"

def test_newline_delimiter():
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6, "'1\\n2,3' should return 6"

def test_custom_delimiter():
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3, "'//;\\n1;2' should return 3"

def test_negative_numbers():
    calculator = StringCalculator()
    with pytest.raises(ValueError, match=r"Negative numbers not allowed: -2"):
        calculator.add("1,-2,3")

