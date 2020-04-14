import pytest
from vlad.problem_4_p_7_vlad import Problem4P7Vlad


class TestProblem4P1(object):
    def instantiate_solution(self):
        return Problem4P7Vlad()

    @pytest.mark.parametrize("x, y, expected", [
        (2.0, 5, 32.0),
        (3.0, 3, 27.0),
        (1.0, 100, 1.0),
        (13412341234, 0, 1)
    ])
    def test_x_to_the_y(self, x, y, expected):
        assert self.instantiate_solution().x_to_the_y(x, y) == expected

