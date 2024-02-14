'''My Calculator Test'''
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Test addition works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test subtraction works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test multiply works'''
    assert multiply(2,2) == 4

def test_division():
    '''Test division works'''
    assert divide(2,2) == 1
    