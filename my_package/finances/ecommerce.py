
def calculate_brutto(netto: float = 0) -> float:
    """
    This Function Calculate Brutto Of Value
    :param netto: Value To Calculate
    :return: Result Calculation
    """
    brutto = netto * 1.23
    return float(f"{brutto:.2f}")


def calculate_netto(brutto: float = 0) -> float:
    """
    This Function Calculate Netto Of Value
    :param brutto: Value To Calculate
    :return: Result Of Calculate
    """
    netto = brutto - (brutto * 0.23)
    return float(f"{netto:.2f}")


def calculate_discount(price: float = 0, list_with_discounts: list = []) -> list:
    """
    This Function Count Discount Value Of Price
    :param price: Price To Count Discounts
    :param list_with_discounts: List Of All Discounts
    :return: List With Calculated Discounts
    """
    if len(list_with_discounts) == 0:
        return [price]

    output = []
    for discount in list_with_discounts:
        output.append(price * discount)

    return output

