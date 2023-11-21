import datetime
import decimal

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


@pytest.fixture
def sms_message():
    sms_message: SmsMessage = SmsMessage(
        'Buy car for 430 dollars, 5454 15.11.23 10:15 amazon authcode 434034',
        'amazon',
        datetime.datetime(2023, 11, 15, 10, 15, 50)
    )
    return sms_message


def test_parse_ineco_expense(sms_message):
    cards: list[BankCard] = [BankCard('5454', 'Will Smith'), BankCard('3434', 'Will Smith')]
    expense_answer: Expense = Expense(decimal.Decimal(430), cards[0], 'amazon', datetime.datetime(2023, 11, 15, 10, 15))
    assert parse_ineco_expense(sms_message, cards) == expense_answer


def test_parse_ineco_expense_wrong_card(sms_message):
    wrong_cards: list[BankCard] = [BankCard('4849', 'Will Smith'), BankCard('5959', 'Will Smith')]
    with pytest.raises(IndexError):
        parse_ineco_expense(sms_message, wrong_cards)
