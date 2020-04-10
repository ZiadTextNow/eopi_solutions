import pytest
from arshan.problem_4_p_1_arshan import Problem4P1Arshan


class TestProblem4P1(object):
    def instantiate_solution(self):
        return Problem4P1Arshan()

    @pytest.mark.parametrize("num, parity", [
        (1, 1),
        (0, 0),
        (1 << 2, 1),
        (1 << 2 | 1 << 4, 0),
    ])
    def test_get_parity(self, num, parity):
        assert self.instantiate_solution().get_parity(num) == parity
