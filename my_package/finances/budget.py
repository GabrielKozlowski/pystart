
def calculate_expenses(expenses: list) -> float:
    """
    This Function Sum Value From List
    :param expenses: List With Value To Sum
    :return: Sum Of List Value
    """

    if len(expenses) == 0:
        return None

    return sum(expenses)


def calculate_monthly_budget(total_income: float = 0, total_expenses: float = 0) -> float:
    """
    This Function Submit Value Of Total Income And Total Expenses And Return Result
    :param total_income: Value Of Total Income
    :param total_expenses: Value Of Total Expenses
    :return: Result Of Calculate
    """
    result = total_income - total_expenses
    return float(f"{result:.2f}")


