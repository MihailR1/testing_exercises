import os
import shutil

import pytest
import faker

from functions.level_4.two_students import Student


@pytest.fixture
def create_student():
    fake = faker.Faker()

    def student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            telegram_account=f"@{fake.user_name()}"):

        new_student = Student(first_name, last_name, telegram_account)

        return new_student

    yield student
    del student


@pytest.fixture
def create_list_with_students(create_student):
    def create_students_list(
            number_students=10,
            include_names: list[tuple[str, str, str]] | None = None):

        students = []

        if include_names:
            students = [create_student(name, second_name, tg)
                        for name, second_name, tg in include_names]

        students += [create_student() for _ in range(number_students)]

        return students

    yield create_students_list
    del create_students_list


@pytest.fixture
def create_file():
    fake = faker.Faker()

    filename = fake.file_name(category='text')
    base_dir = os.path.abspath(os.path.dirname(__file__))
    temp_data_dir = os.path.join(base_dir, 'test_temp_data')
    full_file_path = os.path.join(temp_data_dir, filename)

    os.makedirs(temp_data_dir, exist_ok=True)

    def write_text_to_file(text='AnyText'):
        with open(full_file_path, 'w', encoding='utf-8') as file:
            file.writelines(text)

        return full_file_path

    yield write_text_to_file
    shutil.rmtree(temp_data_dir)


@pytest.fixture
def create_config_file(create_file):
    def add_text(
            config_line='[tool:app-config]\n',
            extra_field_text='extra_fields: sumnum: sum([1,3,4])'):

        file_path = create_file(config_line + extra_field_text)

        return file_path

    return add_text
