import pytest

from functions.level_4.two_students import get_student_by_tg_nickname, Student


@pytest.mark.parametrize(
    'tg_user, tg_to_find',
    [
        (None, ''),
        (None, '@ivanov'),
    ])
def test__get_student_by_tg_nickname__no_tg_users(
        tg_user, tg_to_find, create_list_with_students
):
    list_with_students = create_list_with_students(include_names=[('Ivan', 'Ivanov', tg_user)])

    assert get_student_by_tg_nickname(tg_to_find, list_with_students) is None


@pytest.mark.parametrize(
    'name, last_name, tg',
    [
        ('Ivan', 'Ivanov', '@ivan'),
        ('Petr', 'Ivanov', 'petrotg'),
        ('Vladimir', 'Popov', '@popov'),
        ('Dmitriy', 'Petrov', 'dimpet')
    ]
)
def test__get_student_by_tg_nickname__have_tg_and_matched_student(
        name, last_name, tg, create_list_with_students
):
    list_with_students = create_list_with_students(include_names=[(name, last_name, tg)])

    result = get_student_by_tg_nickname(tg.strip('@'), list_with_students)

    assert isinstance(result, Student)
    assert (result.first_name == name and result.last_name == last_name
            and result.telegram_account == tg)
