import pytest
from vlad.problem_12_p_2_vlad import Problem12P2Vlad


class TestProblem12P2(object):
    def instantiate_solution(self):
        return Problem12P2Vlad()

    @pytest.mark.parametrize("anonymous_letter, text_for_magazine, writable", [
        ('abcd', 'abcd', True),
        ('aabcd', 'abcd', False),
        ('abcd', 'aabcd', True),
    ])
    def test_is_anonymous_letter_writable(self, anonymous_letter, text_for_magazine, writable):
        assert self.instantiate_solution().is_anonymous_letter_constructable(anonymous_letter, text_for_magazine) == writable
