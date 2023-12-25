import pytest

from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize('promocode_len', [1, 3, 4, 5, 9, 232, 29, 3502])
def test__generate_promocode__valid_numbers(promocode_len):
    result = generate_promocode(promocode_len)

    assert len(result) == int(promocode_len)
    assert result.isalpha() is True


@pytest.mark.parametrize('promocode_len', [0, -0, -2, -24, -3502])
def test__generate_promocode__not_valid_numbers(promocode_len):
    assert generate_promocode(promocode_len) == ''
