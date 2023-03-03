
def calculate_brutto(netto: float, vat: float = 0.23) -> float:
    """
    This Function Calculate Brutto Of Value
    :param vat: Vat To Calculate
    :param netto: Value To Calculate
    :return: Result Calculation
    """
    return netto * (1 + vat)


def calculate_netto(brutto: float, vat: float = 0.23) -> float:
    """
    This Function Calculate Netto Of Value
    :param vat: Vat To Calculate
    :param brutto: Value To Calculate
    :return: Result Of Calculate
    """
    return brutto / (1 + vat)


def calculate_discount(total: float, list_with_discounts: list) -> float:
    """
    This Function Count Discount Value Of Price
    :param total: Price To Count Discounts
    :param list_with_discounts: List Of All Discounts
    :return: List With Calculated Discounts
    """

    for discount in list_with_discounts:
        total -= total * discount

    return total

