"""BAD EXAMPLE: Script without __name__ guard.

Problem: The test code runs every time this file is imported!
"""


def calculate_total(prices):
    """Sum all prices."""
    return sum(prices)


def apply_discount(total, percent):
    """Apply percentage discount."""
    return total * (1 - percent / 100)


# BAD: This runs on EVERY import!
print("Running tests...")
result = calculate_total([10, 20, 30])
print(f"Test result: {result}")

# Imagine if this was:
# database.delete_all_records()
