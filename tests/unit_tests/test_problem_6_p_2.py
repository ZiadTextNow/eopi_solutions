import pytest
from vlad.problem_6_p_2_vlad import Problem6P2Vlad


class TestProblem6P2(object):
    def instantiate_solution(self):
        return Problem6P2Vlad()

    @pytest.mark.parametrize("str_b1, b1, b2, str_b2", [
        ('123', 5, 9, '42'),
        ('-123', 5, 9, '-42'),
        ('3', 7, 2, '11'),
        ('-3', 7, 2, '-11'),
        ('333', 3, 10, '39'),
        ('615', 7, 13, '1A7'),
        ('-615', 7, 13, '-1A7'),
        ('1A7', 13, 7, '615'),
        ('-1A7', 13, 7, '-615'),
    ])
    def test_int_to_str(self, str_b1, b1, b2, str_b2):
        assert self.instantiate_solution().base_conversion(str_b1, b1, b2) == str_b2
