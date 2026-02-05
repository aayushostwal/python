"""Utility functions.

Helper functions that support the core functionality.
"""


def calculate(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        Sum of a and b.
        
    Example:
        >>> calculate(2, 3)
        5
    """
    return a + b


def _internal_helper():
    """Private function (underscore prefix convention).
    
    The leading underscore signals to other developers:
    "This is internal, don't rely on it."
    
    It won't be exported with "from module import *"
    """
    pass


def multiply(a: int, b: int) -> int:
    """Multiply two numbers.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        Product of a and b.
    """
    return a * b
