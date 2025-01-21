# IMPORTANT NOTE:- #
Please take clone from main branch, instead of main.


# tdd_calc
Install the Python 3.10 (help: https://realpython.com/installing-python/)
Check version, it should be 3.10.x

<code>python -V</code>

Install the virtual environment maker

<code>apt install python3.10-venv</code>

go to root of this project from terminal and do following steps

Create the virtual environment

<code>python3.10 -m venv venv-3.10</code>

activate env

<code>source venv-3.10/bin/activate</code>

Now install the requirements required to run this project

<code>pip install -r requirements.txt --use-deprecated legacy-resolver</code>

if this runs ok, then setup is done

if you want to deactivate/exit from virtal env

<code>deactivate</code>


# Run the main.py for string calculation
<code>python3 main.py</code>

# Run the test_string_calculator.py to test the function for string calculation

<code>pytest test_string_calculator.py</code>

Note: If you have installed any python lib, pls update the requirement

<code>pip freeze > requirements.txt</code>

