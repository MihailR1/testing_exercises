import datetime
import random

import pytest

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__only_one_expense(create_expense):
    expense = create_expense()
    sum_for_day = expense.amount

    result = calculate_average_daily_expenses([expense])

    assert result == sum_for_day


def test__calculate_average_daily_expenses__in_one_day(create_list_with_expenses):
    list_with_expenses = create_list_with_expenses(
        max_amount=9000, number_transaction=15, is_diffrenet_dates=False)
    sum_for_day = sum([expense.amount for expense in list_with_expenses])

    result = calculate_average_daily_expenses(list_with_expenses)

    assert result == sum_for_day


@pytest.mark.parametrize('number_of_days', [2, 3, 5, 7, 8, 22, 34, 48, 80, 125, 365, 476])
def test__calculate_average_daily_expenses__different_days_range(
        create_list_with_expenses,
        number_of_days):

    dates_list = tuple(
        (datetime.datetime(year=2023, month=random.randint(10, 12), day=random.randint(1, 24))
         for _ in range(number_of_days))
    )
    list_with_expenses = create_list_with_expenses(
        max_amount=9000, number_transaction=15, is_diffrenet_dates=False, dates=dates_list)
    unique_dates = set((expense.spent_at for expense in list_with_expenses))
    mean_for_days = sum((expense.amount for expense in list_with_expenses)) / len(unique_dates)

    result = calculate_average_daily_expenses(list_with_expenses)

    assert result == mean_for_days
