import datetime
import decimal

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
def create_expense():
    def expense(
            amount: decimal.Decimal = decimal.Decimal(430.5),
            currency: Currency = Currency.RUB,
            card: BankCard = BankCard(last_digits='4422', owner='Will Smith'),
            spent_in: str = 'amazon',
            spent_at: datetime.datetime = datetime.datetime.utcnow(),
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
