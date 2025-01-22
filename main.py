import re
from string_calculator import calculateString  # String calc class


if __name__ == "__main__": 
    calc = calculateString()
    try:
        print(calc.add(""))     #blank string as input       
             
        print(calc.add("1"))    #single string as input   

        print(calc.add("1,5"))  #two string with comma separated as input   

        print(calc.add("1\n2,3"))  #new line and comma separated string as input    

        print(calc.add("//;\n1;2"))   #delimeter change to ";" input   

        # This will raise an error
        print(calc.add("1,-2,3"))     #negative string as input   

    except ValueError as e:
        print(e)                                  # Output: Negative numbers not allowed: -2, -3
