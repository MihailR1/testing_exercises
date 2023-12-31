import pytest

from functions.level_4.four_lines_counter import count_lines_in


@pytest.mark.parametrize('filepath', ['123213.jpg', '23123.png', 'test_word.psd', 'audio.mp3'])
def test__count_lines_in__file_not_exist(filepath):
    assert count_lines_in(filepath) is None


@pytest.mark.parametrize(
    'text, result',
    [
        ('  #ttetsetset, etwet\n234234234\n328#', 2),
        ('#test\n #lltle, ks#, \n ##text', 0),
        ('some text', 1),
        ('@tg_name\n some#text, \n #### start text, \n &what', 3),
        ('', 0)
    ])
def test__count_lines_in__files_with_different_text(text, result, create_file):
    file_path = create_file(text)

    assert count_lines_in(file_path) == result
