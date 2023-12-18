import datetime

from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__same_destination_but_in_month(create_expense, create_list_with_expenses):
    service = 'amazon'
    expense = create_expense(spent_in=service)
    list_with_different_expenses = create_list_with_expenses()
    expenses_at_one_month = [
        create_expense(spent_in=service, spent_at=datetime.datetime(2023, 11, day)) for day in range(1, 5)
    ]
    list_with_expenses = list_with_different_expenses + expenses_at_one_month

    result = is_subscription(expense=expense, history=list_with_expenses)

    assert result is False


def test__is_subscription__same_destination_diff_months(create_expense, create_list_with_expenses):
    service = 'hbo'
    expense = create_expense(spent_in=service)
    list_with_different_expenses = create_list_with_expenses()
    expenses_at_different_months = [create_expense(
        spent_in=service, spent_at=datetime.datetime(2023, month, 15)) for month in range(1, 11)]
    list_with_all_expenses = list_with_different_expenses + expenses_at_different_months

    result = is_subscription(expense, list_with_all_expenses)

    assert result is True


def test__is_subscription__any_different_payments(create_expense, create_list_with_expenses):
    expense = create_expense(spent_in='amazon')
    list_with_different_expenses = create_list_with_expenses()

    result = is_subscription(expense, list_with_different_expenses)

    assert result is False
