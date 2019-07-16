from bill_split.bill import Bill


def test_split_one_person_100():
    """
    Splitting a bill with 1 person should have them pay the entire bill.
    """
    bill = Bill(42)
    person = 'John'

    split = bill.split({person: 100})

    assert split[person] == bill.cents


def test_split_one_person_not_100():
    """
    If there is only one person, they should pay the full bill even if
    they are not mapped to 100% of the bill.
    """
    bill = Bill(42)
    person = 'John'

    split = bill.split({person: 50})

    assert split[person] == bill.cents


def test_split_odd_50_50():
    """
    If two people are splitting an odd bill 50/50, the last person
    should pay an extra cent.
    """
    bill = Bill(3)
    p1 = 'John'
    p2 = 'Anne'

    split = bill.split({p1: 50, p2: 50})

    assert split[p1] == 1
    assert split[p2] == 2
