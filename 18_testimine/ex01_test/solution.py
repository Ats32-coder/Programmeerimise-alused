"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if 1 <= time <= 4:
        return False

    if 5 <= time <= 17:
        return coffee_needed

    if 18 <= time <= 24:
        return True


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10

    elif a == b == c:
        return 5

    elif b != a and c != a:
        return 1

    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    max_big_needed = ordered_amount // 5
    big_to_use = min(big_baskets, max_big_needed)
    remaining = ordered_amount - big_to_use * 5

    if remaining <= small_baskets:
        return remaining
    else:
        return -1