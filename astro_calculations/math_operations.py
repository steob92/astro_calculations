from .printing import print_details
import numpy as np

def add(a, b, debug = False):
    """Add two numbers together

    Args:
        a : input value, float or int
        b : input value, float or int
    
    Returns:
        a + b
    """
    if debug:
        print_details(a,b)
    return a + b

def sub(a, b, debug = False):
    """Subtract two numbers together

    Args:
        a : input value, float or int
        b : input value, float or int
    
    Returns:
        a - b
    """
    if debug:
        print_details(a,b)
    return a - b

def mult(a, b, debug = False):
    """Multiply two numbers together

    Args:
        a : input value, float or int
        b : input value, float or int
    
    Returns:
        a * b
    """
    if debug:
        print_details(a,b)
    return a * b

def div(a, b, debug = False):
    """Divide one number by another

    Args:
        a : input value, float or int
        b : input value, float or int
    
    Returns:
        a / b
    """
    if debug:
        print_details(a,b)
    return a / b


def capped_sqrt(a, debug = False):
    """Get the sqrt of a number if it is greater than 0

    Args:
        a : input value, float or int
        
    Returns:
        sqrt(a) if a > 0 otherwise 0 
    """
    if a > 0:
        return np.sqrt(a)
    return 0
