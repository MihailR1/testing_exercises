from functions.level_1.one_gender import genderalize


def test_genderalize():
    verb_male: str = 'MAN'
    verb_female: str = 'FEMALE'
    gender: str = 'male'
    assert genderalize(verb_male, verb_female, gender) == verb_male
    assert genderalize(verb_male, verb_female, 'fem') == verb_female
