from functions.level_2.five_replace_word import replace_word

"""
Случаи для тестирования:
Успешные:
    1 - Подается предложение и слова для замены - на выходе предложение с замененными словами
    2 - Слова в предложении и слова для замены в разном регистре - на выходе регистристр должен сохраниться
    3 - Подается 1 слово и оно же указано в слове на замену - на выходе заменное слово
Крайние случаи:
    1 - Подается пустой текст и слова для замены - ValueError
    2 - Подается текст, но слова для замены пустой текст - ValuError
    3 - Подается текст, но слова на которое меняем нету - ValuError
"""


def test__replace_word__with_text():
    text = 'default text test'
    replace_from = 'text'
    replace_to = 'test'

    result = 'default test test'
    assert replace_word(text, replace_from, replace_to) == result

