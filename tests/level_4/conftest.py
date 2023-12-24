import os
import random
import shutil

import pytest
import faker


@pytest.fixture
def filepaths_list():
    fake = faker.Faker()

    return [
        fake.file_path(depth=random.randint(1, 3), extension='txt')
        for _ in range(10)
    ]


@pytest.fixture
def create_file(filepaths_list):
    filepath = random.choice(filepaths_list)
    base_dir = os.path.abspath(os.path.dirname(__file__))
    temp_data_dir = os.path.join(base_dir, 'test_temp_data')
    file_path = os.path.join(temp_data_dir, filepath)

    os.makedirs(temp_data_dir, exist_ok=True)

    def write_text_to_file(text):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(text)
        return file_path

    yield write_text_to_file

    shutil.rmtree(temp_data_dir)
