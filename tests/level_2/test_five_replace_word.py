import pytest

from functions.level_2.five_replace_word import replace_word

"""
Случаи для тестирования:
Успешные:
    1 - Подается предложение и слова для замены - на выходе предложение с замененными словами
    2 - Подается предложение, в котором несколько слов для замены - все они должны быть заменены
    3, 4 - Подается предложение, но нету слов для замены (2 случая)
    5 - Подает предложение, в предложении нету слов для замены
    6 - Слова в предложении и слова для замены в разном регистре - на выходе регистр должен сохраниться
    7 - Подается 1 слово и оно же указано в слове на замену - на выходе замененное слово
Крайние случаи:
    1 - Подается пустой текст - вернется пустая строка
    2 - Подается ошибочный тип данных (int) - AttributeError
    3 - Слово, которое заменяем, находится в конце предложения и заканчивается точкой "." - замены не будет
"""


@pytest.fixture
def prepare_default_text():
    text = 'Hello world this is default text for pytest'
    text_without_replaced_word = 'Hello world this is default text for '
    return text, text_without_replaced_word


def test__replace_word__standart_success_case(prepare_default_text):
    text, expected_result = prepare_default_text
    replace_from = 'pytest'
    replace_to = 'unittest'
    expected_result += replace_to

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__few_words_for_replace_in_text():
    text = 'Hello WORLD this Is pytest text for PytESt'
    replace_from = 'pytest'
    replace_to = 'UnnitTest'
    expected_result = 'Hello WORLD this Is UnnitTest text for UnnitTest'

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__without_replace_from_word(prepare_default_text):
    text, _ = prepare_default_text
    replace_from = ' '
    replace_to = 'unittest'
    expected_result = text

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__without_replace_to_word(prepare_default_text):
    text, expected_result = prepare_default_text
    replace_from = 'pytest'
    replace_to = ''

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__no_words_for_replace_in_text(prepare_default_text):
    text, _ = prepare_default_text
    replace_from = 'C#'
    replace_to = 'python'
    expected_result = text

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__words_in_different_register():
    text = 'Hello WORLD this Is default text for PytESt'
    replace_from = 'pytest'
    replace_to = 'UnnitTest'
    expected_result = 'Hello WORLD this Is default text for UnnitTest'

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__only_one_word():
    text = 'Hello'
    replace_from = 'hEllo'
    replace_to = 'hi'
    expected_result = replace_to

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__empy_text():
    text = ''
    replace_from = 'pytest'
    replace_to = 'UnnitTest'
    expected_result = text

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result


def test__replace_word__wrong_type_data(prepare_default_text):
    text, _ = prepare_default_text
    replace_from = 84
    replace_to = 'UnnitTest'

    with pytest.raises(AttributeError):
        replace_word(text, replace_from, replace_to)


def test__replace_word___word_endwith_dot(prepare_default_text):
    text, expected_result = prepare_default_text
    text += '.'
    replace_from = 'pytest'
    replace_to = 'UnnitTest'
    expected_result = text

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == expected_result
