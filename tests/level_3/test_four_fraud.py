import random

from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__without_fraud(list_expenses_without_fraud_transactions):
    result = find_fraud_expenses(list_expenses_without_fraud_transactions)

    assert result == []


def test__find_fraud_expenses__with_fraud(list_expenses_with_fraud_transactions):
    result = find_fraud_expenses(list_expenses_with_fraud_transactions)

    assert result != []

