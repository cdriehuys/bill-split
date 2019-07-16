#!/usr/env/python

import logging

from bill_split import config, bill


logging.basicConfig(level=logging.DEBUG)


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
    raw_dollars = read_float("Enter the total to split: $")
    total_bill = bill.Bill.from_dollars(raw_dollars)

    print(f"\n\nSplitting ${total_bill.cents / 100:.2f}\n")

    options = config.read_config_file()
    split_map = options.get('splits', {})

    for person, cents in total_bill.split(split_map).items():
        print(f"  {person}: ${cents / 100:.2f}")


if __name__ == '__main__':
    main()

