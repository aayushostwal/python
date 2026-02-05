"""MyPackage - A demo Python package.

This __init__.py file serves multiple purposes:
1. Marks the directory as a Python package
2. Runs when the package is imported (initialization)
3. Controls the public API via __all__ and imports

Usage:
    import mypackage
    from mypackage import greet, calculate
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# __all__ controls what "from mypackage import *" exports
# Only include stable, documented functions here
__all__ = ["greet", "calculate"]

# Convenient imports - allows users to do:
#   from mypackage import greet
# instead of:
#   from mypackage.core import greet
from .core import greet
from .utils import calculate
