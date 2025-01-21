import re
from string_calculator import StringCalculator #string calculator class 


if __name__ == "__main__": 
    calculator = StringCalculator()
    try:
        print(calculator.add(""))     #blank string as input            
        print(calculator.add("1"))    #single string as input                
        print(calculator.add("1,5"))  #two string with comma separated as input            
        print(calculator.add("1\n2,3"))  #new line and comma separated string as input         
        print(calculator.add("//;\n1;2"))   #delimeter change to ";" input     
        # This will raise an error
        print(calculator.add("1,-2,3"))     #negative string as input           
    except ValueError as e:
        print(e)                                  # Output: Negative numbers not allowed: -2, -3
