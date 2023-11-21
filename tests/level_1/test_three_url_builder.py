import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    'host_name, relative_url, get_params, result_with_params, result_without_params',
    [
        (
                'ya.ru', 'search/', {'text': 'python', 'lr': 11167},
                'ya.ru/search/?text=python&lr=11167',
                'ya.ru/search/'
        ),
        (
                'google.ru', 'search/', {'text': 'python', 'lr': 11167},
                'google.ru/search/?text=python&lr=11167',
                'google.ru/search/'
        ),
    ]
)
def test_build_url(host_name, relative_url, get_params, result_with_params, result_without_params):
    assert build_url(host_name, relative_url, get_params) == result_with_params
    assert build_url(host_name, relative_url) == result_without_params
