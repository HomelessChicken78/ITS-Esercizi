from my_project.calculator import Calculator
'''
def test_addition():
    calculation: Calculator = Calculator(10, 5)
    assert calculation.addition() == 13, "The sum is wrong"

def test_subtraction():
    calculation: Calculator = Calculator(10,5)
    assert calculation.subtraction() == 5, "The subtraction is wrong"

def test_multiplication():
    calculation: Calculator = Calculator(10, 5)
    assert calculation.multiplication() == 50, "The multiplication is wrong"

def test_division():
    calculation: Calculator = Calculator(10,5)
    assert calculation.division() == 2.00, "The division is wrong"
'''


# This allows us to create only one object
import pytest
@pytest.fixture
def calculation():
    return Calculator(10,5)

def test_addition(calculation):
    assert calculation.addition() == 13, "The sum is wrong"

def test_subtraction(calculation):
    assert calculation.subtraction() == 5, "The subtraction is wrong"

def test_multiplication(calculation):
    assert calculation.multiplication() == 50, "The multiplication is wrong"

def test_division(calculation):
    assert calculation.division() == 2.00, "The division is wrong"

# Finally you can use 
# pytest
# To execute all tests

# pytest -v
# also allows you to have a more detailed overview

# pytest <path>::<function test name>
# such as pytest my_project/tests/test_calculator.py::test_addition
# allows only to execute a single test