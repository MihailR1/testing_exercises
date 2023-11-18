import datetime
import decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    sms_message: SmsMessage = SmsMessage(
        'Buy car for 430 dollars, 5454 15.11.23 10:15 amazon authcode 434034',
        'amazon',
        datetime.datetime(2023, 11, 15, 10, 15, 50)
    )
    cards: list[BankCard] = [BankCard('5454', 'Will Smith'), BankCard('3434', 'Will Smith')]
    expense_answer: Expense = Expense(decimal.Decimal(430), cards[0], 'amazon', datetime.datetime(2023, 11, 15, 10, 15))
    assert parse_ineco_expense(sms_message, cards) == expense_answer
