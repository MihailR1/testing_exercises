import pytest

from functions.level_2.three_first import first

"""
Случаи для тестирования:
Успешные:
    1 - Есть список со значениями - вернется 1 элемент
    2 - Список и default заданы - вернет первый элемент списка
    3 - Пустой список и Default значение по умолчанию - вызовет ошибку
    4 - Пустой список и default задано как None, int, str - вернет это значение
Крайние случаи:
    1 - Если default задана строкой, то вернется строка, что функцией не предусмотрено
"""


def test__first__items_not_empty():
    prepare_list = [2, 8]
    expected_result = prepare_list[0]

    result = first(prepare_list)

    assert result == expected_result


@pytest.mark.parametrize(
    'items, default, result',
    [
        ([3, 4, 6, 7], 'hello', 3),
        ([6, 7, 5], None, 6),
        ([9, 7, 5], 5, 9)
    ]
)
def test__first__items_and_default_are_not_empty(items, default, result):
    assert first(items, default) == result


def test__first__items_is_empty_and_default_is_not_set():
    with pytest.raises(AttributeError):
        assert first([])


@pytest.mark.parametrize('default', ['hello', None, 32])
def test__first__items_is_empty_and_default_is_set(default):
    assert first([], default) == default
