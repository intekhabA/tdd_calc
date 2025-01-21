import re
from string_calculator import StringCalculator



# Example usage
if __name__ == "__main__":
    calculator = StringCalculator()
    try:
        print(calculator.add(""))                 # Output: 0
        print(calculator.add("1"))                # Output: 1
        print(calculator.add("1,5"))              # Output: 6
        print(calculator.add("1\n2,3"))           # Output: 6
        print(calculator.add("//;\n1;2"))         # Output: 3
        # This will raise an error
        print(calculator.add("1,-2,3"))           
    except ValueError as e:
        print(e)                                  # Output: Negative numbers not allowed: -2
