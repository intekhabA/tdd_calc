import pytest
from string_calculator import calculateString  # String calc class
calc = calculateString()

def test_empty_string_returns_zero():
    
    assert calc.add("") == 0, "Empty string should return 0"

def test_single_number():
    
    assert calc.add("1") == 1, "'1' should return 1"

def test_two_numbers():
    
    assert calc.add("1,5") == 6, "'1,5' should return 6"

def test_newline_delimiter():
    
    assert calc.add("1\n2,3") == 6, "'1\\n2,3' should return 6"

def test_custom_delimiter():
    
    assert calc.add("//;\n1;2") == 3, "'//;\\n1;2' should return 3"

def test_negative_numbers():
    
    with pytest.raises(ValueError, match=r"Negative numbers not allowed: -2"):
        calc.add("1,-2,3")

