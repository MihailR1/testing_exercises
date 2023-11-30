import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment

"""
Случаи для тестирования:
Успешные:
    1 - Стандартные случаи (4шт): Текст и списки плохих, хороших слов - отработка Good, bad, 2x - None
    
Крайние случаи:
    1 - Слово, которое ищем, находится в конце предложения и заканчивается точкой ". или !"
    2 - Ошибочный тип данных good/bad words, вместо set подали list - тест отработает
    3 - Ошибочный тип данных в text - тест упадет, AttributeErr
"""


class TestCheckTweetSentiment:
    text = 'Hello world this is default test for pytest. Simple test for pytest!'
    good_words = {'world', 'hello'}
    bad_words = {'is', 'this'}

    @pytest.mark.parametrize(
        'good_words, bad_words, result',
        [
            (good_words, bad_words, None),
            ({'no words'}, {'no words'}, None),
            ({'world', 'hello', 'test'}, bad_words, 'GOOD'),
            (good_words, {'world', 'hello', 'test'}, 'BAD')
        ]
    )
    def test__check_tweet_sentiment__standart_success_cases(self, good_words, bad_words, result):
        assert check_tweet_sentiment(self.text, good_words, bad_words) == result

    def test__check_tweet_sentiment__word_endwith_dot(self):
        good_words = self.good_words
        good_words.add('pytest')
        expected_result = None

        assert check_tweet_sentiment(self.text, good_words, self.bad_words) == expected_result

    def test__check_tweet_sentiment__wrong_type_data_in_good_words(self):
        good_words = list(self.good_words)
        expected_result = None

        assert check_tweet_sentiment(self.text, good_words, self.bad_words) == expected_result

    def test__check_tweet_sentiment__wrong_type_data_in_text(self):
        text = list(self.text)

        with pytest.raises(AttributeError):
            assert check_tweet_sentiment(text, self.good_words, self.bad_words)
