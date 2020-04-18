import pytest
from arshan.problem_4_p_1_arshan import Problem4P1Arshan
from vlad.problem_4_p_1_vlad import Problem4P1Vlad


class TestProblem4P1(object):
    def instantiate_solution(self):
        #return Problem4P1Vlad()
        return Problem4P1Arshan()

    @pytest.mark.parametrize("num, parity", [
        (1, 1),
        (0, 0),
        (1 << 2, 1),
        (1 << 2 | 1 << 4, 0),
        (1 << 128, 1),  # big number
        (1 << 1024, 1),
        ((1 << 1024 | 1 << 128), 0)
        #(1 << (1 << 128), 1),  # too big a number
    ])
    def test_get_parity(self, num, parity):
        assert self.instantiate_solution().get_parity(num) == parity
