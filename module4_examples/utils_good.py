"""GOOD EXAMPLE: Module with proper __name__ guard.

The test code only runs when executed directly:
    python utils_good.py

When imported, only the functions are available.
"""


def calculate_total(prices):
    """Sum all prices."""
    return sum(prices)


def apply_discount(total, percent):
    """Apply percentage discount."""
    return total * (1 - percent / 100)


# GOOD: Only runs when executed directly
if __name__ == "__main__":
    print("Running tests...")
    result = calculate_total([10, 20, 30])
    print(f"Test result: {result}")
