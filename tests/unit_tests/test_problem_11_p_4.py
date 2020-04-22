import pytest
from vlad.problem_11_p_4_vlad import Problem11P4Vlad


class TestProblem11P4(object):
    def instantiate_solution(self):
        return Problem11P4Vlad()

    @pytest.mark.parametrize("non_neg_int, int_sqr_root", [
        (0, 0),
        (1, 1),
        (3, 1),
        (4, 2),
        (16, 4),
        (300, 17),
    ])
    def test_integer_square_root(self, non_neg_int, int_sqr_root):
        assert self.instantiate_solution().integer_square_root(non_neg_int) == int_sqr_root
