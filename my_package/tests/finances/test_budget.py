from my_package.finances.budget import calculate_monthly_budget, calculate_expenses

def test_calculate_expenses():
    assert calculate_expenses([100, 200,]) == 300


def test_calculate_monthly_budget():
    assert calculate_monthly_budget(200, 100) == 100