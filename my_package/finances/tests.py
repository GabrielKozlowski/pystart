from my_package.finances.budget import calculate_expenses, calculate_monthly_budget
from my_package.finances.ecommerce import calculate_netto, calculate_brutto, calculate_discount

def test_calculate_expenses():
    assert calculate_expenses([210.4, 190, 222.25, 89.89, 221]) == 933.54
    assert calculate_expenses([]) is None


def test_calculate_monthly_budget():
    assert calculate_monthly_budget(22993.23, 21343.05) == 1650.18
    assert calculate_monthly_budget(21343.05, 22993.23) == -1650.18
    assert calculate_monthly_budget(total_expenses=21343.05) == -21343.05
    assert calculate_monthly_budget(total_expenses=21343.05, total_income=22993.23) == 1650.18
    assert calculate_monthly_budget(22993.23) == 22993.23
    assert calculate_monthly_budget() == 0.0


def test_calculate_brutto():
    assert calculate_brutto(2000) == 2460.00
    assert calculate_brutto(0) == 0.0
    assert calculate_brutto() == 0.0


def test_calculate_netto():
    assert calculate_netto(2000) == 1540.00
    assert calculate_netto(0) == 0.0
    assert calculate_netto() == 0.0


def test_calculate_discount():
    assert calculate_discount(2000, [0.1, 0.2, 0.3, 0.4, 0.5]) == [200, 400, 600, 800, 1000]
    assert calculate_discount(2000) == [2000]
    assert calculate_discount() == [0]
