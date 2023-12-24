import pytest

from functions.level_4.one_brackets import delete_remove_brackets_quotes


def test__delete_remove_brackets_quotes__pass():
    assert delete_remove_brackets_quotes()
