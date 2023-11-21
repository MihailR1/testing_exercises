from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    title: str = 'hello, this is word'
    max_title_length: int = 150
    additional_copy_text: str = 'Copy of'
    expected_result: str = f'{additional_copy_text} {title}'
    assert change_copy_item(title, max_title_length) == expected_result
    assert change_copy_item(title, 25) == title


def test_add_add_number_of_copies_to_title_success():
    title: str = 'Copy of hello, this is word'
    current: str = title
    for i in range(1, 10):
        expected_result: str = f'{title} ({i + 1})'
        assert change_copy_item(current) == expected_result
        current = expected_result


def test_add_add_number_of_copies_to_title_failure():
    title: str = 'Copy of hello, this is word'
    max_title_length: int = 30
    assert change_copy_item(title, max_title_length) == title
