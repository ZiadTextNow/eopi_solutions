import pytest
from vlad.problem_12_p_5_vlad import Problem12P5Vlad


class TestProblem12P5(object):
    def instantiate_solution(self):
        return Problem12P5Vlad()

    @pytest.mark.parametrize("word_list, repeated_word, smallest_distance", [
        (['all', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun' 'and', 'no', 'results'], 'no',
         2),
        (['all', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work'], 'no', 4),
        (['all', 'work', 'and', 'no', 'play', 'makes', 'for', 'big', 'sad'], None, None),
    ])
    def test_nearest_repeated_words(self, word_list, repeated_word, smallest_distance):
        assert self.instantiate_solution().nearest_repeated_words(word_list) == (repeated_word, smallest_distance)
