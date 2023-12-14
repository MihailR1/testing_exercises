import pytest

from functions.level_3.four_fraud import find_fraud_expenses
from functions.level_3.models import Expense


def test__find_fraud_expenses__test(create_expense):
    expense: Expense = create_expense()
    print(expense)
    print(expense.card.last_digits)
