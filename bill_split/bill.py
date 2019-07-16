import logging


logger = logging.getLogger(__name__)


class Bill:
    """
    A representation of a bill.

    .. warning::

        The maximum precision a bill can represent is a single cent. Any
        further precision will be lost.
    """

    def __init__(self, cents: int):
        self.cents = cents
        logger.debug('Created new bill for %d cents', self.cents)

    @classmethod
    def from_dollars(cls, dollars: float):
        return cls(round(dollars * 100))

    def split(self, split_map: dict) -> dict:
        # TODO: Fix 100% split assumption
        logger.debug("Splitting bill for %d cents", self.cents)
        remaining = self.cents
        split_bills = {}
        for i, person in enumerate(split_map):
            if i == len(split_map) - 1:
                partial_sum = remaining
                logger.debug('%s is paying the remaining %d', person, remaining)
            else:
                # Doing integer division here is much easier to understand than
                # trying to understand rounding behavior.
                partial_sum = self.cents * split_map[person] // 100
                logger.debug('%s is paying %d', person, partial_sum)

            remaining -= partial_sum

            split_bills[person] = partial_sum

        if sum(i for i in split_bills.values()) != self.cents:
            logger.warning("Split bill does not match total.")

        return split_bills
