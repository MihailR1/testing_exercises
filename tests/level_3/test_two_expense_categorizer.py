import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category


@pytest.mark.parametrize('service',
                         ['amazon', 'mtv', 'hbo', 'discovery', 'samsung', 'mirpay', 'taxi.ru'])
def test__guess_expense_category__no_category(create_expense, service):
    assert guess_expense_category(create_expense(spent_in=service)) is None


@pytest.mark.parametrize(
    'service, category',
    [
        ('asador./', ExpenseCategory.BAR_RESTAURANT),
        ('.apple.com/bill', ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        ('/.-farm', ExpenseCategory.MEDICINE_PHARMACY),
        (' bastard-', ExpenseCategory.BAR_RESTAURANT),
        ('www.taxi.yandex.ru......', ExpenseCategory.TRANSPORT),
        (',bolt.eu/', ExpenseCategory.TRANSPORT),
        (',/meat house......', ExpenseCategory.SUPERMARKET),
        ('    /tomsarkgh/   . ', ExpenseCategory.THEATRES_MOVIES_CULTURE)
    ]
)
def test__guess_expense_category__have_category_and_allowed_trigger(
        create_expense, service,category):
    assert guess_expense_category(create_expense(spent_in=service)) is category


@pytest.mark.parametrize('service',
                         ['*asador', '/**apple.com/bill', 'bastard??', '..?=chinar', '+sas'])
def test__guess_expense_category__wrong_delimiters(create_expense, service):
    assert guess_expense_category(create_expense(spent_in=service)) is None
