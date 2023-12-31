import pytest

from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize(
    'name, result',
    [
        ('some_name', 'some_name'),
        ('[some_name', '[some_name'),
        ('#{some_name', '#{some_name'),
        ('(some_name', '(some_name'),
        ('"23123123"', '"23123123"')
    ]
)
def test__delete_remove_brackets_quotes__names_without_brackets(name, result):
    assert delete_remove_brackets_quotes(name) == result


@pytest.mark.parametrize(
    'name, result',
    [
        ('{"some_name"}', 'some_name'),
        ('{{text_data}}', 'text_data'),
        ('{some_name', 'ome_na'),
        ('{"some_text', 'some_te'),
        ('{"23123123"}', '23123123')
    ]
)
def test__delete_remove_brackets_quotes__names_with_brackets(name, result):
    assert delete_remove_brackets_quotes(name) == result
