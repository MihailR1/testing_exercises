import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url

"""
Случаи для тестирования:
Успешные:
    1 - Стандартный, успешный случай - вернет True
    2 - Ссылка на файл в pull_request - вернет false
    3 - Ссылка на другой домен - false
    4 - Некорректная ссылка - False
Крайние случаи:
    Что тут может быть крайним случаем понять не могу
"""


@pytest.mark.parametrize(
    'url, result',
    [
        (f'https://github.com/learnpythonru/oop_bases_challenges/pull/20', True),
        (f'https://github.com/learnpythonru/oop_bases_challenges/pull/20/files', False),
        (f'https://gitlab.com/learnpythonru/oop_bases_challenges/pull/20', False),
        (f'github.com/learnpythonru/oop_bases_challenges/pull/20', False)
    ]
)
def test__is_github_pull_request_url__all_cases(url, result):
    assert is_github_pull_request_url(url) is result
