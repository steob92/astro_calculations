from .printing import print_details
import numpy as np
from typing import Union, Optional


def add(
    a: Union[float, int], b: Union[float, int], debug: Optional[bool] = False
) -> Union[float, int]:
    """Add two numbers together

    Args:
        a float,int : input value
        b float,int : input value
        debug bool : whether or not to print debug info. defaults to false

    Returns:
        a + b
    """
    if debug:
        print_details(a, b)
    return a + b


def sub(
    a: Union[float, int], b: Union[float, int], debug: Optional[bool] = False
) -> Union[float, int]:
    """Subtract two numbers together

    Args:
        a float,int : input value
        b float,int : input value
        debug bool : whether or not to print debug info. defaults to false


    Returns:
        a - b
    """
    if debug:
        print_details(a, b)
    return a - b


def mult(
    a: Union[float, int], b: Union[float, int], debug: Optional[bool] = False
) -> Union[float, int]:
    """Multiply two numbers together

    Args:
        a float,int : input value
        b float,int : input value
        debug bool : whether or not to print debug info. defaults to false


    Returns:
        a * b
    """
    if debug:
        print_details(a, b)
    return a * b


def div(
    a: Union[float, int], b: Union[float, int], debug: Optional[bool] = False
) -> Union[float, int]:
    """Divide one number by another

    Args:
        a float,int : input value
        b float,int : input value
        debug bool : whether or not to print debug info. defaults to false


    Returns:
        a / b
    """
    if debug:
        print_details(a, b)
    return a / b


@np.vectorize
def capped_sqrt(a: Union[int, float], debug=False) -> Union[float, int]:
    """Get the sqrt of a number if it is greater than 0

    Args:
        a float,int : input value
        debug bool : whether or not to print debug info. defaults to false


    Returns:
        sqrt(a) if a > 0 otherwise 0
    """
    if a > 0.0:
        return np.sqrt(a)
    return 0.0
