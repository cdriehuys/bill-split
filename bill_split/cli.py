#!/usr/env/python

SPLIT_MAP = {
    'User 1': .25,
    'User 2': .38,
    'User 3': .37,
}


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

    for person, percentage in SPLIT_MAP.items():
        print(f"  {person}: ${total * percentage:.2f}")


if __name__ == '__main__':
    main()

