
def calculate_expenses(expenses: list) -> float:
    """
    This Function Sum Value From List
    :param expenses: List With Value To Sum
    :return: Sum Of List Value
    """

    if len(expenses) == 0:
        return None

    return sum(expenses)


def test_calculate_expenses():
    assert calculate_expenses([210.4, 190, 222.25, 89.89, 221]) == 933.54
    assert calculate_expenses([]) is None


def calculate_monthly_budget(total_income: float = 0, total_expenses: float = 0) -> float:
    """
    This Function Submit Value Of Total Income And Total Expenses And Return Result
    :param total_income: Value Of Total Income
    :param total_expenses: Value Of Total Expenses
    :return: Result Of Calculate
    """
    result = total_income - total_expenses
    return float(f"{result:.2f}")


def test_calculate_monthly_budget():
    assert calculate_monthly_budget(22993.23, 21343.05) == 1650.18
    assert calculate_monthly_budget(21343.05, 22993.23) == -1650.18
    assert calculate_monthly_budget(total_expenses=21343.05) == -21343.05
    assert calculate_monthly_budget(total_expenses=21343.05, total_income=22993.23) == 1650.18
    assert calculate_monthly_budget(22993.23) == 22993.23
    assert calculate_monthly_budget() == 0.0
