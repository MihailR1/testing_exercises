import datetime
import decimal
import random

import pytest

from functions.level_3.models import BankCard, SmsMessage, Currency, ExpenseCategory, Expense


@pytest.fixture
def bank_card():
    card = BankCard(last_digits='4422', owner='Will Smith')
    yield card
    del card


@pytest.fixture
def sms_message():
    sms = SmsMessage(text='Buy at amazon', author='amazon', sent_at=datetime.datetime.utcnow())
    yield sms
    del sms


@pytest.fixture
def popular_stores():
    return ['ozon.ru', 'amazon.ru', 'wildberries.ru', 'walmart.ru', 'yandex.market.ru', 'store.ru',
            'mcdonalds', 'burgerking', 'burgerfree', 'kebabstore', 'lavash&co', 'блинная',
            'lego-store', 'apteka', 'marvel', 'cinemapark']


@pytest.fixture
def different_dates():
    return [
        datetime.datetime(2023, random.randint(10, 11),
                          random.randint(1, 30),
                          random.randint(0, 23)
                          ) for _ in range(10)
    ]


@pytest.fixture
def create_expense():
    def expense(
            amount: decimal.Decimal = decimal.Decimal(430.5),
            currency: Currency = Currency.RUB,
            card: BankCard = BankCard(last_digits='4422', owner='Will Smith'),
            spent_in: str = 'amazon',
            spent_at: datetime.datetime = datetime.datetime(2023, 11, 11, 11, 40),
            category: ExpenseCategory | None = ExpenseCategory.SUPERMARKET
    ):
        created_expense = Expense(
            amount=amount,
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category
        )
        return created_expense

    yield expense
    del expense


@pytest.fixture
def list_expenses_without_fraud_transactions(
        create_expense, popular_stores, different_dates):
    return [
        create_expense(
            spent_in=random.choice(popular_stores),
            spent_at=random.choice(different_dates),
            amount=decimal.Decimal(random.randint(10, 4999))) for _ in range(10)
    ]


@pytest.fixture
def list_expenses_with_fraud_transactions(list_expenses_without_fraud_transactions):
    choice_random = random.choices(list_expenses_without_fraud_transactions, k=2) * 3
    return list_expenses_without_fraud_transactions + choice_random
