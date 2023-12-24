from unittest.mock import patch

import pytest

import functions.level_4.five_extra_fields
from functions.level_4.five_extra_fields import fetch_extra_fields_configuration


def test__fetch_extra_fields_configuration__pass():
    with patch('functions.level_4.five_extra_fields.fetch_app_config_field') as fetch_app_mock:
        fetch_app_mock.return_value = 'some_text'
        fetch_app_mock.call_args_list
    assert fetch_extra_fields_configuration()


def test__show_weather__shows_weater():
    with (
        patch('config.fetch_weather_data') as fetch_weather_data,
        patch('config.print') as print_mock
    ):
        fetch_weather_data.return_value = 30
        show_weather('New-York')
        print_mock.assert_awaited_once_with()
