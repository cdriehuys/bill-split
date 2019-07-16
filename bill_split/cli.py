#!/usr/env/python
import argparse
import logging

from bill_split import config, bill


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_parser():
    """
    Returns:
        The parser used for command line arguments.
    """
    parser = argparse.ArgumentParser(description="Split a bill.")

    parser.add_argument(
        'total',
        help=(
            "The dollar amount of the bill to split. Up to 2 decimal places "
            "may be provided. Any additional precision will be lost."
        ),
        type=float
    )

    return parser


def main():
    """
    Entry point into the program.
    """
    parser = get_parser()
    args = parser.parse_args()

    total_bill = bill.Bill.from_dollars(args.total)
    logger.info("Splitting %s", total_bill)

    options = config.read_config_file()
    split_map = options.get('splits', {})

    for person, cents in total_bill.split(split_map).items():
        print(f"  {person}: ${cents / 100:.2f}")


if __name__ == '__main__':
    main()

