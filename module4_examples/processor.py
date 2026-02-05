"""Professional entry point pattern.

This module demonstrates the recommended structure for Python scripts
that need to work both as importable modules and command-line tools.

Usage:
    python processor.py input.csv output.csv
    python processor.py --help
"""
import sys
from pathlib import Path


def load_data(path: str) -> list:
    """Load data from a file.
    
    Args:
        path: Path to the input file.
        
    Returns:
        List of data items.
    """
    print(f"Loading data from {path}")
    # In a real application, this would read from the file
    return ["item1", "item2", "item3"]


def process_data(data: list) -> list:
    """Transform the data.
    
    Args:
        data: List of items to process.
        
    Returns:
        List of processed items.
    """
    return [item.upper() for item in data]


def save_data(data: list, path: str) -> None:
    """Save processed data to a file.
    
    Args:
        data: Processed data to save.
        path: Output file path.
    """
    Path(path).write_text("\n".join(data))
    print(f"Saved {len(data)} items to {path}")


def main() -> int:
    """Main entry point.
    
    Returns:
        Exit code (0 for success, non-zero for errors).
    """
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input> <output>", file=sys.stderr)
        print(f"Example: {sys.argv[0]} data.csv result.csv", file=sys.stderr)
        return 1
    
    input_path, output_path = sys.argv[1], sys.argv[2]
    
    try:
        data = load_data(input_path)
        processed = process_data(data)
        save_data(processed, output_path)
        print(f"Successfully processed {len(data)} items")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


# Entry point pattern:
# - main() function contains the logic and returns an exit code
# - sys.exit() propagates the exit code to the shell
if __name__ == "__main__":
    sys.exit(main())
