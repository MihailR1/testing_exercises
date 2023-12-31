from unittest.mock import patch

import pytest

from functions.level_4.five_extra_fields import fetch_extra_fields_configuration


def test__fetch_extra_fields_configuration__no_return_value(create_config_file):
    file_path = create_config_file()
    return_value = None

    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as mock:
        mock.return_value = return_value

        assert fetch_extra_fields_configuration(file_path) == {}


@pytest.mark.parametrize(
    'return_value, result',
    [
        ('sumnum: sum([1,3,4])', {'sumnum': 8}),
        ('sorting: sorted(["cba", "abc"])', {'sorting': ["abc", "cba"]}),
        ('print: print("ok")', {'print': None})
    ]
)
def test__fetch_extra_fields_configuration__correct_func_name(
        return_value, result, create_config_file):

    file_path = create_config_file()

    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_mock:
        fetch_app_mock.return_value = return_value
        func_result = fetch_extra_fields_configuration(file_path)

    fetch_app_mock.assert_called_once()
    assert func_result == result


@pytest.mark.parametrize(
    'return_value, result',
    [
        ('sumnum: suma([1,3,4])', {'sumnum': 8}),
        ('sorting: sorting(["cba", "abc"])', {'sorting': ["abc", "cba"]}),
        ('print: printed("ok")', {'print': None})
    ]
)
def test__fetch_extra_fields_configuration__wrong_func_name(
        return_value, result, create_config_file):

    file_path = create_config_file()

    with (pytest.raises(NameError),
          patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_mock):
        fetch_app_mock.return_value = return_value
        func_result = fetch_extra_fields_configuration(file_path)

        assert func_result == result
