import pytest

from functions.level_4.three_promocodes import generate_promocode


def test__generate_promocode__pass():
    assert generate_promocode()
