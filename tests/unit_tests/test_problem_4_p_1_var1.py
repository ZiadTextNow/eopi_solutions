import pytest

from arshan.problem_4_p_1_var1_arshan import Problem4P1Var1Arshan
from vlad.problem_4_p_1_var1_vlad import Problem4P1Var1Vlad


class TestProblem4P1(object):
    def instantiate_solution(self):
        return Problem4P1Var1Arshan()
        return Problem4P1Var1Vlad()

    @pytest.mark.parametrize("num, expected", [
        (0b01010000, 0b01011111),
        (1 << 6 | 1, 1 << 6 | 1),
        (0, 0)
    ])
    def test_right_prop_rightmost_bit(self, num, expected):
        assert self.instantiate_solution().right_prop_rightmost_bit(num) == expected

    @pytest.mark.parametrize("num, power_two, expected", [
        (77, 64, 13),
        (64, 64, 0),
        (5, 1, 0)
    ])
    def test_mod_power_two(self, num, power_two, expected):
        assert self.instantiate_solution().mod_power_two(num, power_two) == expected

    @pytest.mark.parametrize("num, expected", [
        (1, True),
        (2, True),
        (4, True),
        (64, True),
        (3, False),
        (0, False),
        (99, False)
    ])
    def test_is_power_two(self, num, expected):
        assert self.instantiate_solution().is_power_two(num) == expected
