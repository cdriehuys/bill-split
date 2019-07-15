#!/usr/env/python
from bill_split import config


def read_float(prompt: str) -> float:
    """
    Read a floating point number from stdin.

    Returns:
        The next valid floating point number given to stdin.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Entry point into the program.
    """
    total_raw = read_float("Enter the total to split: $")
    total_cents = round(total_raw * 100)
    total = total_cents / 100
    print(f"\n\nSplitting ${total:.2f}\n")

    options = config.read_config_file()

    for person, percentage in options.get('splits', {}).items():
        print(f"  {person}: ${total * percentage / 100:.2f}")


if __name__ == '__main__':
    main()

