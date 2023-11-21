import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    'verb_male, verb_female, gender, result',
    [
        ('man', 'female', 'male', 'man'),
        ('man', 'female', 'None', 'female'),
        ('Сделал', 'Сделала', 'male', 'Сделал'),
        ('Сделал', 'Сделала', 'female', 'Сделала')
    ]
)
def test_genderalize(verb_male, verb_female, gender, result):
    assert genderalize(verb_male, verb_female, gender) == result
