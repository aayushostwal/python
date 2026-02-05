"""Core functionality of the package.

This module contains the main features that users interact with.
"""


def greet(name: str) -> str:
    """Return a greeting message.
    
    Args:
        name: The name to greet.
        
    Returns:
        A greeting string.
        
    Example:
        >>> greet("World")
        'Hello, World!'
    """
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    """Return a farewell message.
    
    Note: This function is NOT in __all__, so it won't be
    exported with "from mypackage import *", but can still
    be imported explicitly.
    
    Args:
        name: The name to bid farewell.
        
    Returns:
        A farewell string.
    """
    return f"Goodbye, {name}!"
