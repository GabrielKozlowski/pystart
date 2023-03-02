
def calculate_brutto(netto: float = 0) -> float:
    """
    This Function Calculate Brutto Of Value
    :param netto: Value To Calculate
    :return: Result Calculation
    """

    return netto * 0.77


def test_calculate_brutto():
    assert calculate_brutto(2000) == 1540.0
    assert calculate_brutto(0) == 0.0
    assert calculate_brutto() == 0.0


def calculate_netto(brutto: float = 0) -> float:
    """
    This Function Calculate Netto Of Value
    :param brutto: Value To Calculate
    :return: Result Of Calculate
    """
    netto = brutto - (brutto * 0.23)
    return float(f"{netto:.2f}")


def test_calculate_netto():
    assert calculate_netto(2000) == 1540.00
    assert calculate_netto(0) == 0.0
    assert calculate_netto() == 0.0
