from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__without_fraud_transactions(create_list_with_expenses):
    list_expenses_without_fraud = create_list_with_expenses(number_transaction=20, max_amount=8000)

    result = find_fraud_expenses(list_expenses_without_fraud)

    assert result == []


def test__find_fraud_expenses__with_fraud_transactions(create_list_with_expenses):
    number_fraud = 5
    list_with_fraud, fraud_expenses = create_list_with_expenses(number_of_fraud_transactions=number_fraud)

    result = find_fraud_expenses(list_with_fraud)

    assert result != []
    assert all(expense in result for expense in set(fraud_expenses))
