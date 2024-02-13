'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test subtraction function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test multiply function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test divide function works '''    
    assert Calculator.divide(2,2) == 1
