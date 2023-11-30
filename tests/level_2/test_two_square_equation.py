import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    'square_coeff, linear_coeff, const_coeff, expected_result',
    [
        (1.5, 3, 7, (None, None)),
        (0, 0, 5, (None, None)),
        (0, 5, 7, (-1.4, None)),
        (-4.4, -32.2, 45, (1.200561239804571, -8.51874305798639)),
        (-544.9, 82.5, 35, (0.3402067017512393, -0.1888027744251244)),
        (544.9, -382.5, -35, (-0.08193873304624845, 0.7839023961036902)),
    ]
)
def test__salve_square_equation(square_coeff, linear_coeff, const_coeff, expected_result):
    assert solve_square_equation(square_coeff, linear_coeff, const_coeff) == expected_result
