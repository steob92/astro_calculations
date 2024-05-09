from .printing import print_details

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
