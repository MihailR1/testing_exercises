from functions.level_1.three_url_builder import build_url


def test_build_url_with_params():
    host_name: str = 'ya.ru'
    relative_url: str = 'search/'
    get_params: dict = {'text': 'python', 'lr': 11167}
    expected_result: str = f'{host_name}/{relative_url}?text={get_params["text"]}&lr={get_params["lr"]}'
    assert build_url(host_name, relative_url, get_params) == expected_result


def test_build_url_without_params():
    host_name: str = 'ya.ru'
    relative_url: str = 'search/'
    expected_result: str = f'{host_name}/{relative_url}'
    assert build_url(host_name, relative_url) == expected_result
